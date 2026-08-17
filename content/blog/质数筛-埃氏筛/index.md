---
title: "质数筛-埃氏筛"
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



void SelectPrimAsh(vector<int>& prim,vector<int>& isprim,int n){
    for(int i=2;i<=n;i++){//i从2开始
        if(isprim[i]==0){
            printf("find a prim %d",i);
            prim.push_back(i);
            for(int j=i*i;j<=n;j+=i){//j可能溢出
                isprim[j]=1;
            }
        }
    }
}

int main(){}
```