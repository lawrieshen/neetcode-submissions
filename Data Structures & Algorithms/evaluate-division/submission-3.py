class DSU:
    def __init__(self):
        self.parent = {}
        self.weight = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0

    def find(self, node):

        if self.parent[node] != node: # b != a
            orig_parent = self.parent[node]
            self.parent[node] = self.find(orig_parent)
            self.weight[node] *= self.weight[orig_parent]
        
        return self.parent[node]

    def union(self, u, v, value):
        self.add(u)
        self.add(v)
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        self.parent[pu] = pv
        self.weight[pu] = value * self.weight[v] / self.weight[u]

        return True

    def get_ratio(self, x, y):
        if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
            return -1.0
        return self.weight[x] / self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = DSU()

        for (a, b), value in zip(equations, values):
            dsu.union(a, b, value)

        return [dsu.get_ratio(a, b) for a, b in queries]