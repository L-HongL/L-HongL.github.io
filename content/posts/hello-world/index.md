
---
title: "Hello World"
date: 2026-08-14
draft: false
---

# Hello World

欢迎来到我的个人博客。

这里主要记录：

- Codeforces
- AtCoder
- ICPC
- 算法竞赛
- C++
- 数学
- 学习笔记

以后会把做过的题、学过的算法以及一些思考记录在这里。
## 数学公式测试

{{< katex >}}

行内公式：

\(SG(x)=mex\{SG(y)\mid x\rightarrow y\}\)

块公式：

$$
SG(x)=mex\{SG(y)\mid x\rightarrow y\}
$$

再测试一个组合数学公式：

$$
\binom{n-1}{k-1}
$$

## C++ 测试

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n);

    for (int &x : a) {
        cin >> x;
    }

    sort(a.begin(), a.end());

    for (int x : a) {
        cout << x << ' ';
    }

    return 0;
}
```