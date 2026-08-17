---
title: "数论分块"
description: "cpp include<bits/stdc++.h using namespace std; define LL long long"
date: 2026-08-15
draft: false
categories:
  - "算法笔记"
tags: []
---
```cpp
#include<bits/stdc++.h>
using namespace std;
#define LL long long

LL Divide_Block(LL x){
    LL l=1,r;
    LL ans=0;
    while(l<=x){
        r=x/(x/l);
        ans+=(x/l)*(r-l+1);
        l=r+1;
    }
    return ans;
}
int main(){}
```