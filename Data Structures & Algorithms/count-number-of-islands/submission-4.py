class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(coordinate: tuple[int, int]):
            
            x, y = coordinate

            # process the node
            grid[x][y] = "0"

            for direction in directions:
                dx, dy = direction
                nx, ny = x + dx, y + dy

                if (0 <= nx < m) and (0 <= ny < n) and (grid[nx][ny] != "0"):
                    dfs((nx, ny))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    dfs((i, j))
                    count += 1

        return count

        # Time: O(m * n)
        # Space: O(1)