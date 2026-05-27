class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid:
            return 0

        m, n = len(grid), len(grid[0])

        maxArea = 0

        def dfs(x, y) -> int:
            if not 0 <= x < m or not 0 <= y < n or grid[x][y] != 1:
                return 0
            
            area = 1

            grid[x][y] = -1

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                area += dfs(nx, ny)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))


        return maxArea