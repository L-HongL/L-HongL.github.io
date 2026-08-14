---
title: "Hong Lo Blog 操作手册"
date: 2026-08-14
draft: false
---

# Hong Lo Blog 操作手册

> Hugo + Blowfish + GitHub Pages
>
> 博客地址：https://l-hongl.github.io/


## 1. 博客技术栈

当前博客使用：

- **Hugo**：静态网站生成器
- **Blowfish**：Hugo 主题
- **GitHub**：保存博客源代码
- **GitHub Actions**：自动构建博客
- **GitHub Pages**：托管最终网页
- **KaTeX**：渲染数学公式

整体流程：

```text
Markdown
   ↓
Hugo
   ↓
HTML
   ↓
GitHub Actions
   ↓
GitHub Pages
   ↓
https://l-hongl.github.io/
````

---

# 2. 本地博客目录结构

当前项目大致结构：

```text
l-hongl.github.io/
│
├── .github/
│   └── workflows/
│       └── hugo.yaml          # GitHub Actions 自动部署
│
├── archetypes/
│   └── default.md             # 新文章默认模板
│
├── assets/                    # 需要 Hugo 处理的资源
│
├── config/
│   └── _default/
│       ├── config.toml        # Hugo 基本配置
│       ├── hugo.toml          # Hugo 配置
│       ├── languages.zh-cn.toml
│       ├── markup.toml        # Markdown / 代码高亮配置
│       ├── menus.zh-cn.toml   # 导航栏
│       ├── module.toml
│       └── params.toml        # Blowfish 主题配置
│
├── content/
│   ├── about/
│   │   └── index.md           # 关于页面
│   │
│   └── posts/
│       ├── hello-world/
│       └── 其他文章/
│
├── layouts/                   # 自定义网页模板
│
├── static/                    # 静态文件
│
├── themes/
│   └── blowfish/              # Blowfish Git submodule
│
├── .gitignore
├── .gitmodules
└── ...
```

---

# 3. 本地启动博客

进入博客目录：

```bash
cd ~/Documents/GitHub/l-hongl.github.io
```

启动 Hugo：

```bash
hugo server
```

然后打开：

```text
http://localhost:1313/
```

Hugo 会自动监视文件变化。

修改 Markdown 后通常不需要重新启动 Hugo，直接刷新网页即可。

停止 Hugo：

```text
Ctrl + C
```

---

# 4. 创建新文章

推荐使用：

```bash
hugo new content/posts/文章目录/index.md
```

例如：

```bash
hugo new content/posts/cf1234a/index.md
```

会生成：

```text
content/
└── posts/
    └── cf1234a/
        └── index.md
```

---

# 5. 新文章 Front Matter

一个推荐的文章开头：

```yaml
---
title: "CF1234A 题解"
date: 2026-08-14
draft: false

categories:
  - Codeforces

tags:
  - DP
  - 数学
---
```

## 常用字段

### title

文章标题：

```yaml
title: "SG 函数学习笔记"
```

### date

发布日期：

```yaml
date: 2026-08-14
```

### draft

是否为草稿：

```yaml
draft: false
```

如果：

```yaml
draft: true
```

默认情况下文章不会出现在正式网站中。

所以新文章如果希望发布：

```yaml
draft: false
```

---

# 6. 分类 Categories

例如 Codeforces：

```yaml
categories:
  - Codeforces
```

AtCoder：

```yaml
categories:
  - AtCoder
```

算法学习：

```yaml
categories:
  - 算法
```

建议博客分类保持简单：

```text
Codeforces
AtCoder
ICPC
算法
随笔
```

不要创建过多分类。

---

# 7. 标签 Tags

标签可以比分类更加细。

例如：

```yaml
tags:
  - DP
  - 博弈论
  - SG函数
```

常用标签可以包括：

```text
DP
图论
博弈论
SG函数
数论
组合数学
线性基
树
字符串
数据结构
贪心
数学
```

---

# 8. Markdown 基本语法

## 一级标题

```markdown
# 标题
```

## 二级标题

```markdown
## 标题
```

## 三级标题

```markdown
### 标题
```

## 粗体

```markdown
**粗体**
```

## 斜体

```markdown
*斜体*
```

## 列表

```markdown
- 第一项
- 第二项
- 第三项
```

---

# 9. 数学公式

博客使用 KaTeX。

## 非常重要

Blowfish 当前的数学公式需要在文章中加入：

```markdown
{{< katex >}}
```

通常在文章第一次使用数学公式之前放一次即可。

例如：

```markdown
## 数学公式

{{< katex >}}

行内公式：

\(SG(x)=mex\{SG(y)\mid x\rightarrow y\}\)

块公式：

$$
SG(x)=mex\{SG(y)\mid x\rightarrow y\}
$$
```

---

## 9.1 行内公式

推荐：

```markdown
\(a^2+b^2=c^2\)
```

显示为：

(a^2+b^2=c^2)

---

## 9.2 块公式

```markdown
$$
SG(x)=mex\{SG(y)\mid x\rightarrow y\}
$$
```

---

## 9.3 常用数学公式

分数：

```latex
\frac{a}{b}
```

组合数：

```latex
\binom{n}{k}
```

求和：

```latex
\sum_{i=1}^{n} a_i
```

极限：

```latex
\lim_{n\rightarrow\infty} a_n
```

集合：

```latex
\{1,2,3,\dots,n\}
```

下标：

```latex
a_i
```

上标：

```latex
a^2
```

矩阵：

```latex
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
```

---

# 10. C++ 代码

使用 Markdown 代码块：

````markdown
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    cout << n << '\n';

    return 0;
}
```
````

一定要写：

```text
cpp
```

这样 Hugo 才能知道这是 C++。

---

# 11. 其他代码语言

Python：

````markdown
```python
print("Hello World")
```
````

Java：

````markdown
```java
System.out.println("Hello World");
```
````

JavaScript：

````markdown
```javascript
console.log("Hello World");
```
````

Bash：

````markdown
```bash
hugo server
```
````

---

# 12. 代码复制

Blowfish 已经配置了代码复制功能。

配置中：

```toml
enableCodeCopy = true
```

因此代码块右上角会出现复制按钮。

一般不需要额外操作。

---

# 13. 文章目录

在：

```text
config/_default/params.toml
```

中确保：

```toml
[article]
  showTableOfContents = true
```

文章使用：

```markdown
## 题目

## 思路

## 状态定义

## 状态转移

## 正确性证明

## 代码

## 复杂度分析
```

Blowfish 会根据标题自动生成目录。

---

# 14. 推荐的算法题解模板

以后写 Codeforces / AtCoder 题解，可以使用：

````markdown
---
title: "CFXXXX 题解"
date: 2026-08-14
draft: false

categories:
  - Codeforces

tags:
  - DP
  - 数学
---

{{< katex >}}

## 题目

简述题目。

## 思路

首先考虑……

## 状态定义

定义：

$$
dp_i = ...
$$

## 状态转移

$$
dp_i = ...
$$

## 正确性证明

说明为什么这个转移是正确的。

## 复杂度分析

时间复杂度：

$$
O(n\log n)
$$

空间复杂度：

$$
O(n)
$$

## C++ 代码

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {

    return 0;
}
````

## 总结

本题的核心是……

````

---

# 15. 创建 About 页面

About 页面：

```text
content/about/index.md
````

修改这个文件即可。

例如：

```markdown
---
title: "关于我"
---

# Hong Lo

ACMer / C++ / Algorithm

这里记录算法竞赛、学习和思考。

主要内容：

- Codeforces
- AtCoder
- ICPC
- 算法与数据结构
- C++
- 数学
```

---

# 16. 修改导航栏

导航栏配置：

```text
config/_default/menus.zh-cn.toml
```

例如：

```toml
[[main]]
  name = "首页"
  pageRef = "/"
  weight = 10

[[main]]
  name = "文章"
  pageRef = "/posts"
  weight = 20

[[main]]
  name = "分类"
  pageRef = "/categories"
  weight = 30

[[main]]
  name = "标签"
  pageRef = "/tags"
  weight = 40

[[main]]
  name = "关于"
  pageRef = "/about"
  weight = 50
```

如果以后想增加：

```text
友链
项目
笔记
```

可以继续添加：

```toml
[[main]]
  name = "项目"
  pageRef = "/projects"
  weight = 60
```

---

# 17. 修改博客基本信息

主要配置：

```text
config/_default/params.toml
```

可以修改：

```toml
[author]
  name = "Hong Lo"
  headline = "ACMer · C++ · Algorithm"
  bio = "记录算法竞赛、学习与思考。"
```

如果以后想修改：

* 博客标题
* 作者
* 简介
* 首页布局
* 文章显示方式
* 暗色模式
* 代码复制
* 目录

优先检查：

```text
config/_default/params.toml
```

---

# 18. 添加图片

静态文件可以放在：

```text
static/
```

例如：

```text
static/images/avatar.jpg
```

那么网站中对应路径：

```text
/images/avatar.jpg
```

Markdown 可以写：

```markdown
![头像](/images/avatar.jpg)
```

---

# 19. Hugo 本地构建

如果想检查正式构建是否成功：

```bash
hugo
```

生成的网站会放在：

```text
public/
```

由于 `.gitignore` 已经忽略：

```text
/public/
```

所以一般不需要提交 `public/`。

---

# 20. GitHub 自动部署

当前博客已经配置：

```text
.github/workflows/hugo.yaml
```

它负责：

```text
push main
   ↓
GitHub Actions
   ↓
下载 Blowfish
   ↓
Hugo build
   ↓
生成 public/
   ↓
GitHub Pages
```

因此：

**以后通常不需要手动执行 `hugo` 再上传网页。**

---

# 21. 发布新文章的完整流程

假设我要写：

```text
CF1234A 题解
```

### 第一步：创建文章

```bash
hugo new content/posts/cf1234a/index.md
```

### 第二步：编辑

打开：

```text
content/posts/cf1234a/index.md
```

写文章。

### 第三步：本地预览

```bash
hugo server
```

打开：

```text
http://localhost:1313/
```

检查：

* 文章是否出现
* 数学公式是否正常
* C++ 代码是否正常
* 图片是否正常
* 分类是否正确
* 标签是否正确

### 第四步：确认不是草稿

确保：

```yaml
draft: false
```

### 第五步：提交 Git

```bash
git add .
```

查看：

```bash
git status
```

然后：

```bash
git commit -m "Add CF1234A solution"
```

### 第六步：推送

```bash
git push
```

### 第七步：等待 GitHub Actions

进入 GitHub：

```text
Actions
```

等待：

```text
Deploy Hugo site to Pages
```

变成：

```text
✅
```

### 第八步：查看网站

```text
https://l-hongl.github.io/
```

---

# 22. 修改已有文章

例如修改：

```text
content/posts/sg-function/index.md
```

修改完成后：

```bash
git add .
git commit -m "Update SG function notes"
git push
```

GitHub Actions 会自动重新部署。

---

# 23. 删除文章

直接删除文章目录：

```bash
rm -rf content/posts/xxx
```

然后：

```bash
git add .
git commit -m "Remove xxx"
git push
```

---

# 24. 修改主题

主题：

```text
themes/blowfish/
```

是 Git submodule。

**不要直接修改里面的主题文件。**

优先使用：

```text
config/
assets/
layouts/
static/
```

进行自定义。

如果需要修改主题模板，可以在：

```text
layouts/
```

中创建对应文件覆盖主题默认模板。

---

# 25. Blowfish 更新

当前 Blowfish 是 Git submodule：

```text
themes/blowfish
```

查看主题状态：

```bash
git submodule status
```

更新主题：

```bash
git submodule update --remote --merge
```

然后：

```bash
git add .
git commit -m "Update Blowfish theme"
git push
```

**如果博客运行正常，不建议频繁更新主题。**

---

# 26. Git 常用命令

查看状态：

```bash
git status
```

查看远程仓库：

```bash
git remote -v
```

添加文件：

```bash
git add .
```

提交：

```bash
git commit -m "说明"
```

推送：

```bash
git push
```

查看提交：

```bash
git log --oneline
```

查看当前分支：

```bash
git branch
```

---

# 27. 最常用的一套命令

以后绝大多数情况下，你只需要：

```bash
# 创建文章
hugo new content/posts/xxx/index.md

# 本地预览
hugo server

# 写完之后
git add .

# 提交
git commit -m "Add xxx"

# 发布
git push
```

就结束了。

---

# 28. 如果网站没有更新

按照下面顺序检查。

## 检查 1：文章是不是草稿

```yaml
draft: false
```

---

## 检查 2：Git 有没有提交

```bash
git status
```

如果看到：

```text
Changes not staged
```

说明还没提交。

---

## 检查 3：有没有 push

```bash
git push
```

---

## 检查 4：GitHub Actions

进入：

```text
GitHub Repository
→ Actions
```

检查：

```text
Deploy Hugo site to Pages
```

是否成功。

---

## 检查 5：本地是否能正常构建

```bash
hugo
```

如果这里报错，说明是 Hugo 配置/文章问题。

---

# 29. 如果 Hugo 报配置错误

可以运行：

```bash
hugo config
```

这个命令主要用于检查 Hugo 最终解析出来的配置。

**不是每次写文章都需要执行。**

---

# 30. 如果数学公式不显示

首先检查文章中是否有：

```markdown
{{< katex >}}
```

例如：

```markdown
{{< katex >}}

行内：

\(a^2+b^2=c^2\)

块公式：

$$
a^2+b^2=c^2
$$
```

如果公式仍然不显示：

1. 检查浏览器控制台
2. 检查 `params.toml`
3. 检查 Blowfish 版本
4. 检查文章中的 `katex` shortcode

---

# 31. GitHub Actions 文件

自动部署文件：

```text
.github/workflows/hugo.yaml
```

当前作用：

```text
main
 ↓
checkout
 ↓
下载 submodule
 ↓
安装 Hugo
 ↓
hugo --gc --minify
 ↓
上传 public
 ↓
GitHub Pages
```

**除非知道自己在做什么，否则不要随意删除这个文件。**

---

# 32. 博客上线后的推荐工作流

以后每天写博客，可以按照：

```text
① 学一道题
       ↓
② 创建 Markdown
       ↓
③ 写题解
       ↓
④ hugo server 本地检查
       ↓
⑤ git add .
       ↓
⑥ git commit
       ↓
⑦ git push
       ↓
⑧ GitHub Actions 自动部署
       ↓
⑨ 博客更新
```

---

# 33. 推荐的文章结构

对于算法竞赛题解，推荐：

```text
题目
 ↓
思路
 ↓
关键观察
 ↓
算法
 ↓
正确性证明
 ↓
复杂度分析
 ↓
代码
 ↓
总结
```

例如：

```markdown
## 题目

## 思路

## 关键观察

## 算法

## 正确性证明

## 复杂度分析

## C++ 代码

## 总结
```

这样长期积累以后，博客会比单纯贴代码更有价值。

---

# 34. 最重要的记忆点

如果以后什么都忘了，只记住下面这几条：

### 启动博客

```bash
hugo server
```

### 创建文章

```bash
hugo new content/posts/xxx/index.md
```

### 数学公式

文章里加入：

```markdown
{{< katex >}}
```

然后使用：

```markdown
\(a+b\)
```

或者：

```markdown
$$
a+b=c
$$
```

### C++ 代码

````markdown
```cpp
// code
```
````

### 发布

```bash
git add .
git commit -m "Update blog"
git push
```

### 正式网站

```text
https://l-hongl.github.io/
```

---

# 35. 当前博客状态

```text
Hugo                         ✅
Blowfish                     ✅
本地开发环境                  ✅
Markdown                     ✅
数学公式 KaTeX               ✅
C++ 代码高亮                 ✅
代码复制                     ✅
文章目录                     ✅
分类                         ✅
标签                         ✅
About 页面                   ✅
GitHub Repository            ✅
GitHub Actions               ✅
GitHub Pages                 ✅
自动部署                     ✅

博客地址：
https://l-hongl.github.io/
```

---

# 36. 最终记忆版

以后新增一篇文章，只需要：

```bash
hugo new content/posts/文章名/index.md
```

写文章。

数学公式：

```markdown
{{< katex >}}

$$
SG(x)=mex\{SG(y)\mid x\rightarrow y\}
$$
```

C++：

````markdown
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    return 0;
}
```
````

然后：

```bash
git add .
git commit -m "Add new post"
git push
```

等待 GitHub Actions 完成。

完成。

---

> **核心思想：**
>
> **Hugo 负责把 Markdown 变成网页，Blowfish 负责网页样式，GitHub 保存源代码，GitHub Actions 自动构建，GitHub Pages 负责最终展示。**

