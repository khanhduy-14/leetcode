class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x: str) -> int:
        if x not in self.parent:
            self.parent[x] =  x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if root_x < root_y:
            self.parent[root_y] = root_x
        elif root_x > root_y:
            self.parent[root_x] = root_y

        return True

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU()

        for i in range(len(s1)):
            dsu.union(s1[i], s2[i])
        res = list(baseStr)
        for i in range(len(res)):
            res[i] = dsu.find(res[i])
        return ''.join(res)