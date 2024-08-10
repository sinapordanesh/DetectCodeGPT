class Trie:
    class Node:
        def __init__(self,c):
            self.c=c
            self.next_c_id={}
            #self.common=0
            self.end=-1

    def __init__(self):
        self.trie=[self.Node('')]
    
    def add(self,id,s):
        i=0
        now=0
        ary=[0]
        while i<len(s) and s[i] in self.trie[now].next_c_id:
            now=self.trie[now].next_c_id[s[i]]
            ary.append(now)
            #self.trie[now].common+=1
            i+=1
        while i<len(s):
            self.trie[now].next_c_id[s[i]]=len(self.trie)
            now=len(self.trie)
            ary.append(now)
            self.trie.append(self.Node(s[i]))
            #self.trie[now].common+=1
            i+=1
        self.trie[now].end=id
        return ary
    
    def search(self,s):
        i=0
        now=0
        ary=[0]
        while i<len(s) and s[i] in self.trie[now].next_c_id:
            now=self.trie[now].next_c_id[s[i]]
            ary.append(now)
            i+=1
        if i<len(s):return []
        return ary
def main(s):
    tr=Trie()
    s.sort(key=lambda x:len(x))
    ans=0
    for i,x in enumerate(s):
        ary=tr.add(i,x)
        seen=set(())
        while ary:
            id=ary.pop()
            for nv in seen&tr.trie[id].next_c_id.keys():
                if tr.trie[tr.trie[id].next_c_id[nv]].end>=0 and tr.trie[tr.trie[id].next_c_id[nv]].end!=i:
                    ans+=1
            seen.add(tr.trie[id].c)
    print(ans)

if __name__=='__main__':
    a2n=lambda x:ord(x)-ord('a')
    n=int(input())
    s=[list(map(a2n,list(input()))) for _ in range(n)]
    [x.reverse() for x in s]
    main(s)
