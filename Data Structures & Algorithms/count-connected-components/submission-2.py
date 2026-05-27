class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n)) # each node is its own parent initially
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            
            return False # means they are already connected

        # do union on each edge
        for a, b in edges:
            union(a, b)
        
        # count distinct roots (aka the number of connected components)
        return sum(1 for i in range(n) if find(i) == i)