class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < prevHeight:
                return

            visit.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, visit, heights[r][c])

        for row in range(m):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, n - 1, atlantic, heights[row][n - 1])

        for col in range(n):
            dfs(0, col, pacific, heights[0][col])
            dfs(m - 1, col, atlantic, heights[m - 1][col])

        return list(pacific.intersection(atlantic))
            
            

            
