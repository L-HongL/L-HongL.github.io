---
title: "二维前缀和"
description: "cpp include<bits/stdc++.h using namespace std; define LL long long int n,m; void add(int x,int y,vector<vector<long long"
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
int n,m;
void add(int x,int y,vector<vector<long long>>& a,LL v){
    a[x][y]+=v;
}

void prefix_sum(vector<vector<LL>>& a){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++)a[i][j]+=a[i][j-1]+a[i-1][j]-a[i-1][j-1];
    }
}

LL query(int x1,int y1,int x2,int y2,vector<vector<long long>>& a){
    return a[x2][y2]+a[x1-1][y1-1]-a[x2][y1-1]-a[x1][y2-1];
}

int main(){}
```