---
title: "week135"
---

https://ac.nowcoder.com/acm/contest/129582/A
ans=n/3*3

https://ac.nowcoder.com/acm/contest/129582/B
公式整理即为数组中每个数减去其下标都要相等，对数计数即可

https://ac.nowcoder.com/acm/contest/129582/C
操作的限制是序列小于等于三时，不能完全排序，特判即可

https://ac.nowcoder.com/acm/contest/129582/D
答案为平均数向上取整

https://ac.nowcoder.com/acm/contest/129582/E
dp,需要注意的是，第二维不只三位，可能会增加或者减少多次，所以设置为5才对    

https://ac.nowcoder.com/acm/contest/129582/F
对每个格子单独计算贡献。
我们能够找到本身是孤立点的设定好的黑色格子，将一个点设为孤立点，其余的(n*m-k-n-m+2)个格子可以任取。
有num1个这样的点，那么他们的贡献是num1*(2^(n*m-k-n-m+2))

同理可以得到剩下的能构造成孤立点的未设点，若将其设为孤立点，其贡献为2^(n*m-k-n-m+1),有(n-numx)*(n-numy)个这样的点、

对以上结果求和取模即可
