class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == 0:
                    return 0
            
            grid[r][c] = 0

            area = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                area += dfs(nr, nc)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea