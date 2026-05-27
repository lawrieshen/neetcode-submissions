class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        max_area = 0

        def bfs(x, y):
            queue = deque([(x, y)])
            area = 0
            while queue:
                x, y = queue.pop()
                if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] != 1:
                    continue

                area += 1
                grid[x][y] = -1

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    queue.append((nx, ny))

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))

        return max_area
