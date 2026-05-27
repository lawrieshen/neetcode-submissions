class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        max_area = 0

        def dfs(x, y):
            if not (0 <= x < m) or not(0 <= y < n) or grid[x][y] != 1:
                return 0

            grid[x][y] = -1
            
            area = 1

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = dx + x, dy + y
                area += dfs(nx, ny)
            return area

        for i in range(m):
            for j in range(n):
                max_area = max(max_area, dfs(i, j))

        return max_area
