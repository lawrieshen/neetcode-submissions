class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # A tree’s minimum-height roots are its center(s): either 1 or 2 nodes.
        # Repeatedly remove all current leaves (indegree 1). The last 1–2 nodes left are the roots of Minimum Height Trees.

        # build a graph first while constructing a indegree

        # iteratively pruning till we find the center
        if n < 2:
            return list(range(n))

        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        queue = deque()

        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                leaf = queue.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)


        return list(queue)
