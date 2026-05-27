class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()

        # enque all the chest
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))
