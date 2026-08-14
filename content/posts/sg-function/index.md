---
title: "SG 函数学习笔记"
date: 2026-08-14
draft: false
categories:
  - 算法
tags:
  - 博弈论
  - SG函数
---

## 1. 什么是 SG 函数

对于一个状态 $x$，定义：

{{< katex >}}

$$
SG(x)=mex\{SG(y)\mid x\rightarrow y\}
$$

其中 $mex$ 表示最小没有出现的非负整数。

## 2. 为什么需要 SG 函数

...

## 3. 代码

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    return 0;
}