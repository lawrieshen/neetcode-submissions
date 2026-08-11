class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific = set()
        # atlantic = set()

        # m = len(heights)
        # n = len(heights[0])

        # def dfs(r, c, visit, prevHeight):
        #     if (r, c) in visit or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < prevHeight:
        #         return

        #     visit.add((r, c))
        #     for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #         nr, nc = dr + r, dc + c
        #         dfs(nr, nc, visit, heights[r][c])

        # for row in range(m):
        #     dfs(row, 0, pacific, -1)
        #     dfs(row, n - 1, atlantic, -1)

        # for col in range(n):
        #     dfs(0, col, pacific, -1)
        #     dfs(m - 1, col, atlantic, -1)

        # return list(pacific.intersection(atlantic))

        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        def dfs(x, y, visit, prevHeight):
            if (x, y) in visit or x < 0 or x >= m or y < 0 or y >= n or heights[x][y] < prevHeight:
                return

            visit.add((x, y))
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                dfs(nx, ny, visit, heights[x][y])

        for r in range(m):
            dfs(r, 0, pacific, -1)
            dfs(r, n - 1, atlantic, -1)

        for c in range(n):
            dfs(0, c, pacific, -1)
            dfs(m - 1, c, atlantic, -1)

        return list(pacific.intersection(atlantic))
        