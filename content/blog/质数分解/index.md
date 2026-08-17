---
title: "质数分解"
description: "cpp include<bits/stdc++.h using namespace std;"
date: 2026-08-15
draft: false
categories:
  - "算法笔记"
tags: []
---
```cpp
#include<bits/stdc++.h>
using namespace std;


vector<int> a;
int n;

void PrimNum(int x){
    int num=0;
    for(int i=2;i*i<=x;i++){
        if(x%i==0){
            printf("找到质因数%d",i);
            while(x%i==0)x/=i;
            num++;
        }
    }
    if(x>1){
        printf("找到质因数%d",x);
        num++;
    }
}


int main(){}
```