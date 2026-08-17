---
title: "裴蜀定理"
description: "裴蜀定理，又译贝祖定理 给出不全为零的整数a，b，存在任意整数x，y，都有gcd(a,b)|ax+by。存在x，y，满足ax+by=gcd(a,b);"
date: 2026-08-15
draft: false
categories:
  - "数学"
tags: []
---
裴蜀定理，又译贝祖定理
给出不全为零的整数a，b，存在任意整数x，y，都有gcd(a,b)|ax+by。存在x，y，满足ax+by=gcd(a,b);

证明：
设d为gcdab，则有整数u，v满足：a=du，b=dv
则有ax+by=d(ux+vy)
因为(ux+vy)为整数，所以可以证明任意不全为0的x和y满足：d|ax+by

要证明存在x和y成立，如果b为0，那么必定存在d=a，x和y必定存在(1,0)
如果a和b都为正整数，那么可以利用辗转相除法：
a=q1*b+r1;->(b,r1)
b=q2*r1+r2;->(r1,r2)
r1=q3*r2+r3;->(r2,r3)
...
rn-3=qn-1*rn-2+rn-1;->(rn-2,rn-1)
rn-2=qn*rn-1+rn;->(rn-1,rn)
rn-1=qn+1*rn;return;

rn=d,将其返回带入
得d=rn-2-qn*rn-1
得rn-1=rn-3-qn-1*rn-2
带入得
d=(1+qn*qn-1)*rn-2-qn*rn-3
如此消去了rn-1，继续消去，最终得到公式d=x*a+y*b



