class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = {}
        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for child in graph[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n
        