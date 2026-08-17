---
title: "容斥定理"
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

int Rong_Chi(int flo,vector<LL>& NsPrim){
    int k=NsPrim.size();
    int ans=0;

    for(int s=1;s<(1<<k);s++){
        int mid=1;
        int cnt=0;
        for(int i=0;i<k;i++){
            if(s>>i&1){
                mid*=NsPrim[i];
                cnt++;
            }
        }
        if(cnt&1){
            ans+=flo/mid;
        }
        else ans-=flo/mid;
    }
    return ans;
}//返回并集后的元素个数
int main(){}
```