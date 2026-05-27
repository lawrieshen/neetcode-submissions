class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.rank[pv] += self.rank[pu]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) + 1 # 1-index
        
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        