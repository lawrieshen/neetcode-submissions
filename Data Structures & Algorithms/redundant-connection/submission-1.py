class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dsu
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False # already connected

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
            
            return True # connect successfully

        last_redundant = None  # Store the last redundant edge
        for x, y in edges:
            if not union(x, y):
                last_redundant = [x, y]
        
        return last_redundant

        return []