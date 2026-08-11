class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            next_leaves = []
            for leaf in leaves:
                nei = adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei]) == 1:
                    next_leaves.append(nei)
            leaves = next_leaves

        return leaves