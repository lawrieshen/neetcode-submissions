class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if len(edges) != n - 1:
        #     return False

        # parent = list(range(n))

        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]

        # def union(x, y):
        #     rootX = find(x)
        #     rootY = find(y)

        #     if rootX == rootY:
        #         return False
            
        #     parent[rootY] = rootX
        #     return True

        # for u, v in edges:
        #     if not union(u, v):
        #         return False

        # return True

        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par) -> bool:
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visit) == n