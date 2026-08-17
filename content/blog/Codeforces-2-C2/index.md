---
title: "Codeforces 2 C2"
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
    LL ans=1e18;
    LL ax,n;cin>>ax>>n;
    LL axx=ax;
    
    vector<int> a(n+1,0);
    vector<int> axs;
    if(ax==0)axs.pu(0);
    while(axx){
        axs.pu(axx%10);
        axx/=10;
    }
    axs.pu(0);reverse(all(axs));
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }

    int m=axs.size()-1;
    vector<vll> dpmin(17+3,vll(n+1,-1));
    LL midmin=0;
    for(int i=1;i<=n;i++)dpmin[0][i]=0;
    for(int i=1;i<axs.size();i++){
        midmin=midmin*10+axs[i];
        for(int j=1;j<=n;j++){
            for(int k=1;k<=n;k++){
                LL mid=dpmin[i-1][k]*10+a[j];
                if(midmin-mid>=0){
                    dpmin[i][j]=max(dpmin[i][j],mid);
                }
            }
        }
    }
    for(int i=1;i<=n;i++){
        if(dpmin[m][i]!=-1&&abs(ans-ax)>abs(dpmin[m][i]-ax)){
            ans=dpmin[m][i];
        }
    }
    
    vector<vll> dp1min(17+3,vll(n+1,-1));
    midmin=axs[1];
    //for(int i=1;i<=n;i++)dp1min[1][i]=0;
    for(int i=2;i<axs.size();i++){
        midmin=midmin*10+axs[i];
        for(int j=1;j<=n;j++){
            for(int k=1;k<=n;k++){
                LL mid=dp1min[i-1][k]*10+a[j];//cout<<a[j]<<"\n";
                if(i==2)mid=a[j];
                if(midmin-mid>=0){
                    dp1min[i][j]=max(dp1min[i][j],mid);
                }
            }
        }
    }
    for(int i=1;i<=n;i++){
        if(dp1min[m][i]!=-1&&abs(ans-ax)>abs(dp1min[m][i]-ax)){
            ans=dp1min[m][i];//cout<<1;
        }
    }
    
        vector<vll> dpmax(17+3,vll(n+1,1e18));
        for(int i=0;i<=n;i++){
            dpmax[0][i]=a[i];
        }
        LL midmax=0;
        for(int i=1;i<axs.size();i++){
            midmax=midmax*10+axs[i];
            for(int j=1;j<=n;j++){
                for(int k=1;k<=n;k++){
                    LL mid=dpmax[i-1][k]*10+a[j];//cout<<mid<<"\n";
                    if(mid-midmax>=0){//cout<<dpmax[i][j]<<" "<<i<<"\n";
                        dpmax[i][j]=min(dpmax[i][j],mid);
                    }
                }
            }
        }
        for(int i=1;i<=n;i++){
            if(abs(ans-ax)>abs(dpmax[m][i]-ax)){
                ans=dpmax[m][i];
                //cout<<dpmax[m][i]<<" "<<i<<"\n";
            }
        }
    
    vector<vll> dp1max(17+3,vll(n+1,1e18));
        for(int i=0;i<=n;i++){
            dp1max[0][i]=0;
        }
        midmax=0;
        for(int i=1;i<axs.size();i++){
            midmax=midmax*10+axs[i];
            for(int j=1;j<=n;j++){
                for(int k=1;k<=n;k++){
                    LL mid=dp1max[i-1][k]*10+a[j];//cout<<mid<<"\n";
                    if(mid-midmax>=0){//cout<<dpmax[i][j]<<" "<<i<<"\n";
                        dp1max[i][j]=min(dp1max[i][j],mid);
                    }
                }
            }
        }
        for(int i=1;i<=n;i++){
            if(abs(ans-ax)>abs(dp1max[m][i]-ax)){
                ans=dp1max[m][i];
                //cout<<dpmax[m][i]<<" "<<i<<"\n";
            }
        }

    cout<<abs(ans-ax)<<'\n';
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