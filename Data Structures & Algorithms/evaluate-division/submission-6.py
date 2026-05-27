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

        # invariant: value(x) = weight[x] * value(root_x)

        # u/ v = value
        # value(u) = weight(u) * value(pu); value(v) = weight(v) * value(pv)
        # value(u) / value(v) = value

        # after parent(pu) = pv

        # value(pu) = weight(pu) * value(pv)

        # value(u) / value(v) = value

        # weight(u) * weight(pu) * value(pv) 
        # ---------------------               = value
        # weight(v) * value(pv)

        # weight(u) * weight(pu)
        # ---------------------               = value
        # weight(v)

        # weight(pu) = value * weight(v) / weight(u)

        self.parent[pu] = pv
        self.weight[pu] = value * self.weight[v] / self.weight[u]

        return True


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = DSU()

        for (a, b), value in zip(equations, values):
            dsu.union(a, b, value)

        # execute the coputation
        res = []
        for x, y in queries:
            if x not in dsu.parent or y not in dsu.parent or dsu.find(x) != dsu.find(y):
                res.append(-1.0)
                continue
            # value(x)   weight(x) * value(root_x)    weight(x)
            # -------- = ------------------------- =  ---------
            # value(y)   weight(y) * value(root_y)    weight(y)
            res.append(dsu.weight[x] / dsu.weight[y])
        return res