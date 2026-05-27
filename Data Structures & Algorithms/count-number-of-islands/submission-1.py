class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        
        # input check
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        count = 0

        def dfs(x, y):
            # base case

            if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] != '1':
                return

            # processthe node
            grid[x][y] = "#" # mark visited

            # explore neighbors
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1'):
                    count += 1
                    dfs(i, j)

        return count