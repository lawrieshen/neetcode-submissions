class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim
        n = len(points)
        visited = set()
        min_heap = [(0, 0)] # (cost to attach, point index)
        total = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue

            visited.add(i)
            total += cost

            xi, yi = points[i]

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    heapq.heappush(min_heap, (abs(xi - xj) + abs(yi - yj), j))

        return total 