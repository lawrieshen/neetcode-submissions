class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return []

        res = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < m or not 0 <= nc < n or grid[nr][nc] == '0':
                    continue
                dfs(nr, nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res