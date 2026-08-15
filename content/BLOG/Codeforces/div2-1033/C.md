---
title: "C"
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

vector<vector<vector<LL>>> a(11,vector<vector<LL>>(11));
struct edg{
    LL x;
    LL k;
    LL i; 
    bool operator<(const edg& other) const{
        return x<other.x;
    }
};

void babason(){    
    LL n,m;cin>>n>>m;
    vector<LL> a;
    vector<LL> b;
    LL mid=m-n;
    a.pu(1);
    for(LL i=n;i>1;i--){
        if(mid>=i-1){
            a.pu(i);
            mid-=i-1;
        }
        else b.pu(i);
    }
    if(mid>0||mid<0){
        cout<<"-1\n";
    }
    else{
        sort(all(a));
        cout<<a.back();
        for(int i=1;i<a.size();i++){
            cout<<a[i]<<" "<<a[i-1]<<"\n";
        }
        for(int i=0;i<b.size();i++){
            cout<<1<<" "<<b[i]<<"\n";
        }
    }

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