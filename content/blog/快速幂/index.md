---
title: "快速幂"
description: "cpp include<bits/stdc++.h using namespace std; long long mod;"
date: 2026-08-15
draft: false
categories:
  - "算法笔记"
tags: []
---
```cpp
#include<bits/stdc++.h>
using namespace std;
long long mod;

long long qpow(long long a,long long m){
    long long ans=1;
    long long mid=a;
    while(m){
        if(a&1){
            ans=(ans*mid)%mod;
        }
        mid=mid*mid%mod;
        m>>=1;
    }
    return ans;
}

int main(){}
```