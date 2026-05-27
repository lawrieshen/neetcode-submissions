class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # dfs

        graph = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))

        def dfs(src, target, visited):
            if src not in graph or target not in graph:
                return -1
            if src == target:
                return 1

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1:
                        return result * weight

            return -1

        return [dfs(q[0], q[1], set()) for q in queries]