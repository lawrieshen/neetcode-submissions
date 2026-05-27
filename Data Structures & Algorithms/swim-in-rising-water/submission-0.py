class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [[grid[0][0], 0, 0]] # (min time to able, x, y)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited.add((0, 0))
        while min_heap:
            time, x, y = heapq.heappop(min_heap)
            if x == n - 1 and y == n - 1:
                return time
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in visited:
                    continue

                visited.add((nx, ny))
                heapq.heappush(min_heap, [max(time, grid[nx][ny]), nx, ny])