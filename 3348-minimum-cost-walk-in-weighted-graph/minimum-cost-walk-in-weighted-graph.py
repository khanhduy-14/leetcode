class Dsu:
    def  __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.weight = [-1] * n
    def find(self, v):
        if self.parent[v] == v:
            return v
        p = self.find(self.parent[v])
        self.parent[v] = p
        return p
    def union(self, a, b, w):
        va = self.find(a)
        vb = self.find(b)
        if vb != va:
            if self.rank[va] < self.rank[vb]:
                va, vb = vb, va
            self.parent[vb] = va
            if self.rank[va] == self.rank[vb]:
                self.rank[va]+=1
        self.weight[va] = self.weight[vb] = self.weight[va] & self.weight[vb] & w
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = Dsu(n)
        res = []
        for a,b,w in edges:
            dsu.union(a,b,w)
    
        for a,b in query:
            va = dsu.find(a)
            vb = dsu.find(b)
            if  va != vb:
                res.append(-1)
            else:
                res.append(dsu.weight[va])
        return res
        