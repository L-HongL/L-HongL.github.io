#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hugo BLOG -> blog 自动迁移脚本
================================
用途：
1. 不删除原来的 content/BLOG
2. 新建 content/blog
3. 把文章 Markdown 转成 Hugo Page Bundle：
      xxx.md -> xxx/index.md
4. 尽量保留文章同目录下的图片/附件
5. 自动添加 categories / tags / date
6. 尽量根据原目录判断分类
7. 自动避免 slug 冲突
8. 默认只执行“预览模式”，确认无误后再真正复制

使用：
    python migrate_blog.py

真正执行：
    python migrate_blog.py --apply

如果脚本不在 Hugo 项目根目录：
    python migrate_blog.py "D:\\你的\\hugo项目"

推荐第一次：
    python migrate_blog.py

确认输出没问题后：
    python migrate_blog.py --apply
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path


# ============================================================
# 配置
# ============================================================

SOURCE_NAME = "BLOG1"
TARGET_NAME = "blog"

# 原一级目录 -> Hugo category
CATEGORY_MAP = {
    "atcode": "AtCoder",
    "atcoder": "AtCoder",
    "Codeforces": "Codeforces",
    "codeforces": "Codeforces",
    "Niuke": "牛客",
    "niuke": "牛客",
    "牛客": "牛客",
    "左程云算法": "算法笔记",
    "积累算法板子": "算法笔记",
    "证明": "数学",
    "数学": "数学",
    "铜牌算法": "算法笔记",
}

# 这些目录通常不是“文章分类”，而是比赛/专题的中间目录
IGNORED_TAG_DIRS = {
    "AC",
    "ac",
    "DIV1",
    "DIV2",
    "DIV3",
    "div1",
    "div2",
    "div3",
    "ED",
    "ed",
}


# ============================================================
# 工具函数
# ============================================================

def eprint(*args):
    print(*args, file=sys.stderr)


def yaml_quote(s: str) -> str:
    """生成安全的 YAML 双引号字符串。"""
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def slugify(text: str) -> str:
    """
    生成比较适合 Hugo URL 的 slug。
    中文保留；空格/特殊字符转为 -。
    """
    text = text.strip()

    # 去掉常见 Markdown / 文件名符号
    text = re.sub(r'[<>:"/\\|?*#%&{}$!@+=`~^]', " ", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-.")

    if not text:
        return "untitled"

    return text[:100]


def read_text(path: Path) -> str:
    """
    尽可能兼容常见编码。
    """
    encodings = [
        "utf-8-sig",
        "utf-8",
        "gb18030",
        "gbk",
    ]

    for enc in encodings:
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            pass

    raise UnicodeDecodeError(
        "unknown",
        b"",
        0,
        1,
        f"无法读取文件：{path}"
    )


def write_text(path: Path, text: str):
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_front_matter(text: str):
    """
    解析最简单的 YAML front matter。
    只提取 title/date/description/categories/tags/draft 等字段。
    不依赖 PyYAML。
    """
    result = {}

    if not text.startswith("---"):
        return result

    parts = text.split("---", 2)
    if len(parts) < 3:
        return result

    fm = parts[1]

    current_list_key = None

    for raw_line in fm.splitlines():
        line = raw_line.rstrip()

        m = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()

            if value == "":
                current_list_key = key
                result[key] = []
            else:
                current_list_key = None
                result[key] = value.strip('"').strip("'")

            continue

        m = re.match(r"^\s*-\s+(.*)$", line)
        if m and current_list_key:
            result.setdefault(current_list_key, []).append(
                m.group(1).strip().strip('"').strip("'")
            )

    return result


def remove_front_matter(text: str) -> str:
    """
    删除原 front matter，迁移时重新生成。
    """
    if not text.startswith("---"):
        return text

    end = text.find("\n---", 3)
    if end == -1:
        return text

    body = text[end + len("\n---"):]

    return body.lstrip("\r\n")


def get_title(path: Path, text: str) -> str:
    fm = parse_front_matter(text)

    title = fm.get("title")

    if isinstance(title, str) and title.strip():
        return title.strip()

    # 没有 title 时使用文件名
    return path.stem


def normalize_title(
    title: str,
    source_file: Path,
    source_root: Path,
) -> str:
    """
    对特别简短的比赛题目标题做适度增强。
    不会修改正常标题。
    """

    parts = source_file.relative_to(source_root).parts

    # 一级分类
    category_dir = parts[0] if parts else ""

    # 只有 title 很短时才考虑增强
    short = title.strip()

    if category_dir.lower() in {"atcode", "atcoder"}:
        # 例如 title=451，路径中有 ABC451
        for p in parts:
            m = re.search(r"ABC\s*([0-9]+)", p, re.I)
            if m:
                if re.fullmatch(r"[A-Za-z]?\d+[A-Za-z]?", short):
                    return f"AtCoder ABC{m.group(1)} {short}".strip()

    if category_dir.lower() == "codeforces":
        # 例如路径 div2-1098 + C2
        contest = None
        for p in parts:
            m = re.search(r"(?:div|edu|ecf|round)[-_ ]?(\d+)", p, re.I)
            if m:
                contest = m.group(1)
                break

        if contest and len(short) <= 5:
            return f"Codeforces {contest} {short}"

    return short


def get_category(source_file: Path, source_root: Path) -> str:
    parts = source_file.relative_to(source_root).parts

    if not parts:
        return "其他"

    first = parts[0]

    return CATEGORY_MAP.get(first, first)


def get_tags(source_file: Path, source_root: Path, title: str):
    """
    根据路径自动产生少量 tags。
    不强行猜题目知识点，避免生成错误标签。
    """

    parts = source_file.relative_to(source_root).parts

    tags = []

    category = get_category(source_file, source_root)

    # 平台标签
    if category in {"AtCoder", "Codeforces", "牛客"}:
        tags.append(category)

    # ABCxxx
    for p in parts:
        m = re.search(r"ABC\s*(\d+)", p, re.I)
        if m:
            tags.append(f"ABC{m.group(1)}")

    # 比赛编号
    for p in parts:
        m = re.search(r"(?:div|edu|ecf|round)[-_ ]?(\d+)", p, re.I)
        if m:
            tags.append(m.group(0).replace("_", "-"))
            break

    # 不把文件夹中的 AC/DIV3 等机械地全部塞进 tags
    # 只保留不会太杂的标签

    # 去重
    result = []
    seen = set()

    for tag in tags:
        if tag and tag not in seen:
            seen.add(tag)
            result.append(tag)

    return result


def get_date(source_file: Path, fm: dict) -> str:
    """
    优先保留原 date。
    没有 date 时使用文件修改时间。
    """
    date = fm.get("date")

    if isinstance(date, str) and date.strip():
        # 只保留日期部分
        m = re.search(r"\d{4}-\d{2}-\d{2}", date)
        if m:
            return m.group(0)

    try:
        timestamp = source_file.stat().st_mtime
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    except OSError:
        return datetime.now().strftime("%Y-%m-%d")


def get_description(fm: dict, body: str, title: str) -> str:
    description = fm.get("description")

    if isinstance(description, str) and description.strip():
        return description.strip()

    # 从正文第一段提取一个简短 description
    paragraphs = re.split(r"\n\s*\n", body.strip())

    for p in paragraphs:
        p = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", p)
        p = re.sub(r"\[[^\]]+\]\([^)]*\)", "", p)
        p = re.sub(r"[#>*`]", "", p)
        p = re.sub(r"\s+", " ", p).strip()

        if len(p) >= 10:
            return p[:120]

    return f"{title} 的学习笔记与整理。"


def build_front_matter(
    title: str,
    description: str,
    category: str,
    tags: list[str],
    date: str,
    original_fm: dict,
) -> str:

    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"description: {yaml_quote(description)}",
        f"date: {date}",
        "draft: false",
        "categories:",
        f"  - {yaml_quote(category)}",
    ]

    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {yaml_quote(tag)}")
    else:
        lines.append("tags: []")

    # 保留一些常用字段
    for key in ("author", "series"):
        value = original_fm.get(key)

        if isinstance(value, str) and value.strip():
            lines.append(f"{key}: {yaml_quote(value.strip())}")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def safe_target_dir(target_root: Path, slug: str) -> Path:
    """
    防止两个文章产生相同 slug。
    """
    candidate = target_root / slug

    if not candidate.exists():
        return candidate

    i = 2
    while True:
        candidate = target_root / f"{slug}-{i}"
        if not candidate.exists():
            return candidate
        i += 1


# ============================================================
# 迁移
# ============================================================

def collect_articles(source_root: Path):
    """
    收集所有 .md。
    排除 _index.md。
    """
    articles = []

    for path in source_root.rglob("*.md"):
        if path.name.lower() == "_index.md":
            continue

        articles.append(path)

    return sorted(articles)


def make_plan(source_root: Path, target_root: Path):
    articles = collect_articles(source_root)

    plan = []

    used_slugs = set()

    for source_file in articles:
        try:
            text = read_text(source_file)
        except Exception as exc:
            eprint(f"[读取失败] {source_file}: {exc}")
            continue

        fm = parse_front_matter(text)
        body = remove_front_matter(text)

        raw_title = get_title(source_file, text)
        title = normalize_title(raw_title, source_file, source_root)

        category = get_category(source_file, source_root)
        tags = get_tags(source_file, source_root, title)
        date = get_date(source_file, fm)
        description = get_description(fm, body, title)

        slug = slugify(title)

        # 避免同名文章
        base_slug = slug
        i = 2
        while slug in used_slugs:
            slug = f"{base_slug}-{i}"
            i += 1

        used_slugs.add(slug)

        target_dir = target_root / slug

        plan.append({
            "source": source_file,
            "target_dir": target_dir,
            "target_md": target_dir / "index.md",
            "text": text,
            "body": body,
            "front_matter": fm,
            "title": title,
            "category": category,
            "tags": tags,
            "date": date,
            "description": description,
            "slug": slug,
        })

    return plan


def print_plan(plan, source_root: Path, target_root: Path):
    print()
    print("=" * 72)
    print("迁移预览")
    print("=" * 72)
    print(f"文章数量：{len(plan)}")
    print(f"源目录：  {source_root}")
    print(f"目标目录：{target_root}")
    print()

    for i, item in enumerate(plan, 1):
        rel = item["source"].relative_to(source_root)

        print(f"[{i:02d}] {rel}")
        print(f"     -> {item['slug']}/index.md")
        print(f"     title:    {item['title']}")
        print(f"     category: {item['category']}")
        print(f"     tags:     {', '.join(item['tags']) or '(无)'}")
        print(f"     date:     {item['date']}")
        print()


def copy_article_files(item, target_dir: Path):
    """
    复制 Markdown 所在目录的附件。

    这样图片相对路径仍然保持：
        ![](image.png)

    如果附件与文章同名等特殊情况，优先保留。
    """
    source_md = item["source"]
    source_dir = source_md.parent

    target_dir.mkdir(parents=True, exist_ok=True)

    # 复制同目录下的非 md 文件
    for child in source_dir.iterdir():
        if child.is_file() and child.suffix.lower() != ".md":
            destination = target_dir / child.name

            if destination.exists():
                # 不覆盖已有文件
                continue

            shutil.copy2(child, destination)


def apply_plan(plan, target_root: Path):
    if target_root.exists():
        print()
        print(f"警告：目标目录已经存在：{target_root}")
        answer = input("继续？输入 YES 才会继续：").strip()

        if answer != "YES":
            print("已取消。")
            return False

    target_root.mkdir(parents=True, exist_ok=True)

    # 创建 blog/_index.md
    index = target_root / "_index.md"

    if not index.exists():
        write_text(
            index,
            """---
title: "博客"
description: "算法竞赛、数学与学习笔记"
---
"""
        )

    for item in plan:
        target_dir = item["target_dir"]
        target_dir.mkdir(parents=True, exist_ok=True)

        fm = build_front_matter(
            title=item["title"],
            description=item["description"],
            category=item["category"],
            tags=item["tags"],
            date=item["date"],
            original_fm=item["front_matter"],
        )

        write_text(
            item["target_md"],
            fm + item["body"].lstrip()
        )

        copy_article_files(item, target_dir)

    print()
    print("=" * 72)
    print("迁移完成")
    print("=" * 72)
    print(f"新博客目录：{target_root}")
    print(f"文章数量：{len(plan)}")
    print()
    print("原来的 BLOG 没有删除。")
    print()
    return True


# ============================================================
# 主程序
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Hugo BLOG 自动迁移为 Page Bundle 博客结构"
    )

    parser.add_argument(
        "project",
        nargs="?",
        default=".",
        help="Hugo 项目根目录，默认是当前目录",
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="真正执行迁移；不加此参数时只预览",
    )

    args = parser.parse_args()

    project_root = Path(args.project).resolve()

    source_root = project_root / "content" / SOURCE_NAME
    target_root = project_root / "content" / TARGET_NAME

    print("=" * 72)
    print("Hugo BLOG 自动迁移工具")
    print("=" * 72)
    print(f"项目目录：{project_root}")
    print()

    if not project_root.exists():
        eprint(f"错误：项目目录不存在：{project_root}")
        sys.exit(1)

    if not (project_root / "hugo.toml").exists() and not (
        project_root / "config"
    ).exists():
        print("警告：当前目录看起来不像 Hugo 项目根目录。")
        print("请确认里面存在 hugo.toml 或 config/。")
        print()

    if not source_root.exists():
        eprint(f"错误：找不到：{source_root}")
        eprint("请把脚本放在 Hugo 项目根目录运行，或者传入项目路径。")
        sys.exit(1)

    if target_root.exists() and args.apply:
        print(f"错误：目标目录已经存在：{target_root}")
        print("为了避免覆盖你的文件，脚本不会自动删除它。")
        print("请先删除/改名 content/blog，或者手动确认后再运行。")
        sys.exit(1)

    plan = make_plan(source_root, target_root)

    if not plan:
        print("没有找到文章 Markdown。")
        return

    print_plan(plan, source_root, target_root)

    if not args.apply:
        print("=" * 72)
        print("这是【预览模式】，没有修改任何文件。")
        print()
        print("如果预览结果正确，请运行：")
        print()
        print("    python migrate_blog.py --apply")
        print()
        print("Windows 也可以直接双击运行脚本进行预览。")
        print("=" * 72)
        return

    print("=" * 72)
    print("准备开始真正迁移。")
    print("原 content/BLOG 不会删除。")
    print("=" * 72)

    answer = input("确认执行？输入 YES：").strip()

    if answer != "YES":
        print("已取消。")
        return

    apply_plan(plan, target_root)


if __name__ == "__main__":
    main()