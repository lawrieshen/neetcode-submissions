class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) # map a -> a list of [b, b/a]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/ values[i]))

        def dfs(src, target, visited):
            if src not in adj or target not in adj:
                return -1
            if src == target:
                return 1

            visited.add(src)

            for nei, ratio in adj[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)

                    if result != -1:
                        return result * ratio

            return -1

        return [dfs(q[0], q[1], set()) for q in queries]

        # Time: O((V + E) * Q)
        # Sapce: O(V + E)