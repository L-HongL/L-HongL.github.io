---
title: "普通线性基模板"
description: "cpp include<bits/stdc++.h using namespace std; int BIT=60; vector<long long basis(BIT+1,0); bool zero1=0; bool insert_xo"
date: 2026-08-15
draft: false
categories:
  - "算法笔记"
tags: []
---
```cpp
#include<bits/stdc++.h>
using namespace std;
int BIT=60;
vector<long long> basis(BIT+1,0);
bool zero1=0;
bool insert_xor(long long x){
    for(int i=BIT;i>=0;i--){
        if((x>>i)&1){
            if(basis[i]!=0){
                basis[i]=x;
                return true;
            }
            x^=basis[i];
        }
    }
    return false;
}

void build_xor(vector<long long>& a,int n){
    for(int i=1;i<=n;i++){
        zero1|=(!insert_xor(a[i]));
    }
}

int main(){}
```