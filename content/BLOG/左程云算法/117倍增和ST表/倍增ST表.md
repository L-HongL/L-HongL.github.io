---
title: "倍增ST表"
---

```cpp
#include<bits/stdc++.h>
using namespace std;
#define LL long long 
#define vll vector<LL>


void build(vector<vll>& st,vector<int>& log2,vector<LL>& a,int n){
    log2[0]=-1;
    for(int i=1;i<=n;i++){
        
        log2[i]=log2[i>>1]+1;
    }
    st.resize(n+1,vll(log2[n]+1,0));
    for(int i=1;i<=n;i++){
        st[i][0]=a[i];
    }
    for(int k=1;k<=log2[n];k++){
        for(int i=1;i+(1<<k)-1<=n;i++){
            st[i][k]=max(st[i][k-1],st[i+(1<<(k-1))][k-1]);
        }
    }
}


int main(){}
```