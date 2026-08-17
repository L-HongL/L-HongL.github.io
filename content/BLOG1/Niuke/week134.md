---
title: "week134"
---

https://ac.nowcoder.com/acm/contest/129231/A
语法题

https://ac.nowcoder.com/acm/contest/129231/B
数学优化，对铜牌重复除九即为循环得到的金牌

https://ac.nowcoder.com/acm/contest/129231/C
操作总是会增加前缀，所以整个序列是递减的，要统计获得的最多种类数，可以将序列的每个下标的最大值递推出来后，定义一个数模拟即可

https://ac.nowcoder.com/acm/contest/129231/D
有两种解法：
1.滑动窗口
对于这种连续的子区间，我们使用滑动窗口维护可用子区间，同时用两个单调队列用于维护子区间是否只有两种差值小于1的数。

2.动态规划
对于连续的子区间，计算价值是可以继承的，所以维护一个三个状态的dp数组，表示当前下标-1，0，+1的数能达到的最大子序列长度

https://ac.nowcoder.com/acm/contest/129231/E
颅内模拟一遍发现可以直接算出答案

