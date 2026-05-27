class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in edges:
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return [x, y]

            parent[rootY] = rootX