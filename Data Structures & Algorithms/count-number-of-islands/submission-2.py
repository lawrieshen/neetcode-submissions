class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs

        # input check
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        
        count = 0

        def bfs(x, y):
            queue = deque([(x, y)])

            while queue:
                x, y = queue.pop()

                if not (0 <= x < m) or not (0 <= y < n) or (grid[x][y] != '1'):
                    continue

                # process node
                grid[x][y] = "#"

                # explore neighbors
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1'):
                    count += 1
                    bfs(i, j)

        return count        