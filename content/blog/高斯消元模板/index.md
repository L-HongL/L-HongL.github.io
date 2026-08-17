---
title: "高斯消元模板"
description: "cpp include<bits/stdc++.h using namespace std; int BIT=60; bool zero1=0; void build(vector<long long& a,int n){ int len="
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
bool zero1=0;
void build(vector<long long>& a,int n){
    int len=1;
    for(int i=BIT;i>=0;i--){
        for(int j=len;j<=n;j++){
            if((a[j]>>i)&1){
                swap(a[len],a[j]);
                break;
            }
        }
        if((a[len]>>i)&1){
            for(int j=1;j<=n;j++){
                if(j!=len&&((a[j]>>i)&1)){
                    a[j]^=a[len];
                }
            }
            len++;
        }
    }
    len--;
    zero1= len!=n;
    reverse(a.begin()+1,a.begin()+len+1);
}

int main(){}
```