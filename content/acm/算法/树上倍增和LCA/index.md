
+++
title = '树上倍增和LCA'
date = '2026-09-10T11:35:17+08:00'
draft = false


tags = ['算法学习']
categories = ['算法']

author = 'Luo Hong'

showReadingTime = true
showTableOfContents = true
showWordCount = true
+++
## 树上倍增求LCA
基本思想：
1. 利用st表+二进制优化查询。st[i][j]表示第i位，向父节点跳$2^j$次，得到的节点。
2. 有两个要查询的节点，将深度较深的节点跳到与另一个节点深度相同，判断两点是否相遇。若未相遇，两个点跳跃到最浅不相等的祖先节点a,b，返回答案st[a][0]或者st[b][0]

先把两个点放到同一高度，再让它们一起尽可能往上跳，但绝不跳到 LCA 上面。
```
struct lca{
    int st[5000][32];
    int dep[5000];
    int n;
    vector<vector<int>> a;

    void dfs(int x,int las,int de){//建立st表
        st[x][0]=las;
        dep[x]=de;
        for(int i=1;(1<<i)<=dep[x];i++){
            st[j][i]=st[st[j][i-1]][i-1];
        }
        for(auto v:a[x]){
            if(v==las)continue;
            dfs(v,x,de+1);
        }
    }

    void init(vector<vector<int>> b){//初始化
        a=b;n=b.size()-1;
        dfs(1,0,1);
    }

    int query(int x,int y){//查询
        if(dep[x]>dep[y]){
            swap(x,y);
        }
        for(int i=31;i>=0;i--){
            if(dep[st[y][i]]>=dep[x]){
                y=st[y][i];
            }
        }
        if(a==b)return a;
        for(int i=31;i>=0;i--){
            if(st[y][i]!=st[x][i]){
                y=st[y][i];
                x=st[x][i];
            }
        }
        return st[x][0];
    }
};
```
## Tarjan求LCA
基本思想：
1. dfs递归节点，当一个节点S的子树遍历完后，开始处理所有包含节点S的询问。
2. 询问的两个点S和x中，如果另一个点x已经递归过了，那么答案便记录为x所属并查集的代表节点，代表节点必须是并查集所有节点的最高祖先。如果x没有被递归过，那么就跳过该询问，等到x处理询问时再记录答案。
3. 处理完所有节点后，将S节点与他的子树并起来。

DFS 负责决定什么时候处理，vis 判断另一个点有没有处理过，并查集负责找到当前的祖先
```
struct tarjan{
    vector<vector<int>> q,a;
    map<pair<int,int>,int> ma;

    vector<int> fa;
    vector<bool> vis;

    int root(int x){
        int t=x;while(fa[t]!=t){t=fa[t];}
        while(x!=fa[x]){
            int mi=fa[x];
            fa[x]=t;
            x=mi;
        }
        return t;
    }
    void bin(int xx,int yy){
        int x=root(xx),y=root(yy);
        if(x!=y){
            fa[y]=x;
        }
    }

    void init(vector<vector<int>> p,vector<vector<int>> b){
        q=p;a=b;

        for(int i=0;i<=a.size();i++){
            fa[i].pu(i);
        }
    }

    void query(int x,int las){
        vis[x]=1;
        for(auto v:a[x]){
            if(v==las)continue;
            query(v,x);
            bin(x,v);
            for(auto u:q[v]){
                if(vis[u]){
                    ma[{v,u}]=root(u);
                }
            }
        }
    }
};
```