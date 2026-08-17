---
title: "E"
description: "cpp include<bits/stdc++.h using namespace std; define LL long long define pii pair<int,int define pll pair<LL,LL define "
date: 2026-08-15
draft: false
categories:
  - "AtCoder"
tags:
  - "AtCoder"
  - "ABC456"
---
```cpp
#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pu push_back
#define pk pop_back
#define all(a) (a).begin(),(a).end()
#define vii vector<int>
#define vll vector<LL>
#define se second
#define fi first
const LL mod=1e9+7;


struct edg{
    LL x;
    LL k;
    LL i; 
    bool operator<(const edg& other) const{
        return x<other.x;
    }
};

void babason(){    
    int n,m;cin>>n>>m;
    vector<vii> a(n+10);
    for(int i=1;i<=m;i++){//for循环的限制条件写错了变量名
        int x,y;cin>>x>>y;
        a[x].pu(y);
        a[y].pu(x);
    }

    int w;cin>>w;
    vector<vii> ma(w*n+n);
    vector<string> s(n+10);
    for(int i=1;i<=n;i++){
        cin>>s[i];
        a[i].pu(i);
    }

    vector<int> head(n*w+n,0);
    for(int j=0;j<w;j++){
        for(int i=1;i<=n;i++){
            if(s[i][j]=='x')continue;
            for(auto v:a[i]){
                if(s[v][(j+1)%(w)]=='o'){
                    ma[j*n+i].pu((j+1)%(w)*n+v);
                    head[(j+1)%(w)*n+v]++;
                }
            }
        }
    }

    //vector<bool> vis(n*w+1,0);
    queue<int> q;
    for(int i=1;i<=n*w;i++){
        if(head[i]==0)q.push(i);
    }

    int num=q.size();
    while(q.size()){
        int x=q.front();q.pop();
        for(auto v:ma[x]){
            head[v]--;
            if(head[v]==0){
                q.push(v);num++;
            }
        }
    }

    if(num!=n*w){
        cout<<"Yes\n";
    }
    else cout<<"No\n";

}
int main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);
    int t;cin>>t;while(t--)
    babason();
    return 0;
}
```