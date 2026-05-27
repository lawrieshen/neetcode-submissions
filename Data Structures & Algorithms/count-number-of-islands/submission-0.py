class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        count = 0

        def dfs(x, y):
            # base case

            if not 0 <= x < m or not 0 <= y < n or grid[x][y] != '1':
                return
            
            # process the current cell
            grid[x][y] = '#' # mark as visited

            # explore neighbors
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
                
            