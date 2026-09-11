
+++
title = '字典树'
date = '2026-09-10T11:16:40+08:00'
draft = false


tags = ['算法学习']
categories = ['算法']

author = 'Luo Hong'

showReadingTime = true
showTableOfContents = true
showWordCount = true
+++


## 静态字典树
基本思想：利用链式前向星构建一个树，树上每个节点都有27个子节点，分别表示27个字母，子节点存下一个节点的数组下标。
```
struct Trie{
    int tr[50000][27];
    int num[50000];
    int tot=0;

    void insert(string s){
        int now=0;
        for(auto v:s){
            int x=v-'a';
            if(tr[now][x]==0){
                tr[now][x]=++tot;
            }

            now=tr[now][x];
            num[now]++;//若把这句放到此for循环中，表示计算前缀串。
        }
        //num[now]++;//若把这句放到此for循环外，表示记录出现过该字符串
    }


    bool find(string s){
        int now=0;
        for(auto v:s){
            int x=v-'a';
            now=tr[now][x];
        }
        if(now==0) return 0;
        return num[now];
    }
};
```