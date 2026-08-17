---
title: "Codeforces 2 D1"
description: "cpp include<bits/stdc++.h using namespace std; define LL long long define pii pair<int,int define pll pair<LL,LL define "
date: 2026-08-15
draft: false
categories:
  - "Codeforces"
tags:
  - "Codeforces"
  - "div2"
---
```cpp
#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pk push_back
#define pu push_back
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
    int n,k;cin>>n>>k;
    LL ans=0;
    string s1,s2;cin>>s1>>s2;
    LL s1num1=0,s1num0=0;
    LL s2num1=0,s2num0=0;
    
    string s3;
    for(int i=0;i<n;i++){
        if(s1[i]=='0')s1num0++;
        else s1num1++;
        if(s2[i]=='0')s2num0++;
        else s2num1++;
        
        if(s1[i]!=s2[i]){
            s3+="1";
        }
        else s3+="0";
    }
    
    LL s3num0=0,s3num1=0;
    for(int i=0;i<n;i++){
        if(s3[i]=='0')s3num0++;
        else s3num1++;
    }

      ans=(s1num1*s1num0+s2num1*s2num0);
    LL numlr=1;
    LL nummid=0;
    for(int i=1;i<=k;i++){
        if(i%2==1){
            ans+=numlr*(s3num1*s3num0);
           
            ans+=nummid*(s1num1*s1num0+s2num1*s2num0); 
            nummid+=numlr;numlr+=nummid;
        }
        else{
            
            
        }
        //cout<<ans<<" ";
    }
    //cout<<'\n';
    cout<<ans<<'\n';
    //cout<<'\n';
}
int main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);
    int t;cin>>t;while(t--)
    babason();
    return 0;
}
//010                             110
//010             100             110  +1
//010     110     100     010     110  +0
//010 100 110 010 100 110 010 100 110  +2

// 1 1         0 0
// 1 0 1       1 1
// 1 1 0 1 1   0 1
// 1 0 1 1 0 1 1 0 1   2 3
// 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1    2 5
// 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 10 11
```