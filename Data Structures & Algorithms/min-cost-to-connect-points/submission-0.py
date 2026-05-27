class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # return the min cost to connect all points tgt -> MST (prim's or kruskal's)

        # implement prim

        # bfs + min_haep + visited check + update rule := min(weight, v)

        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([distance, j])
                graph[j].append([distance, i])

        res = 0
        visited = set()
        min_heap = [[0, 0]] # weight, index in points
        
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue

            # process the node
            res += cost
            visited.add(i)

            # step deeper
            for next_cost, next_i in graph[i]:
                if next_i not in visited:
                    heapq.heappush(min_heap, [next_cost, next_i])
        
        return res
        