---
title: "week132"
description: "https://ac.nowcoder.com/acm/contest/128672/A 语法题"
date: 2026-08-15
draft: false
categories:
  - "牛客"
tags:
  - "牛客"
---
https://ac.nowcoder.com/acm/contest/128672/A
语法题

https://ac.nowcoder.com/acm/contest/128672/B
判断题，对于5的倍数，个位必须是0或5，所以查询是否有数位是0或5即可

https://ac.nowcoder.com/acm/contest/128672/C
贪心，要想相邻元素不是互质的，首先当前数必须与前面一位数不互质，如果前一个数经过替换，那我们可以把他替换成与左右相邻的数不互质的数，这样可以这个数必定与前一个数不互质，若这个数与前一个数互质，表示必须要替换，则num++。

https://ac.nowcoder.com/acm/contest/128672/D
数学优化，根据公式我们知道，要对1e5数据的所有二元配对，将二元求和除二，并向下取整
将公式展开发现展开式极其类似(数据和*(n-1)-向下取整减少的数值)/2，只有奇数+偶数会减少数值，所以统计有多少对奇数+偶数即可。

https://ac.nowcoder.com/acm/contest/128672/E
BFS，对于两种操作，我们不知道那种状态最优，并且由于暴力搜索范围在2e6，所以可以考虑模拟暴搜，使用bfs搜索最少操作数

https://ac.nowcoder.com/acm/contest/128672/F
对每一个字符串求最小连续数组和，求出答案即可