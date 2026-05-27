class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        m = len(grid)
        n = len(grid[0])
        INF = 2**31 - 1
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))