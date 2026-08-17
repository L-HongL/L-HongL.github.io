---
title: "二维差分"
description: "cpp include<bits/stdc++.h using namespace std; define LL long long int n,m; void add(int x1,int y1,int x2,int y2,vector<"
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
void add(int x1,int y1,int x2,int y2,vector<vector<long long>>& a,LL v){
    a[x1][y1]+=v;
    if(y2<m){a[x1][y2+1]-=v;}
    if(x2<n){a[x2+1][y1]-=v;}
    if(x2<n&&y2<m){a[x2+1][y2+1]+=v;}
}

void prefix_sum(vector<vector<LL>>& a){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++)a[i][j]+=a[i][j-1];
    }
    for(int j=1;j<=m;j++){
        for(int i=1;i<=n;i++)a[i][j]+=a[i-1][j];
    }
}

LL query(int x,int y,vector<vector<long long>>& a){
    return a[x][y];
}

int main(){}
```