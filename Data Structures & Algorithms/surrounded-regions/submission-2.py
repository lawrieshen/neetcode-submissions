class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # register all 'O' on the border
        # loop over the grid
        # if we found a an 'O' and not on the border we filp it by implementing dfs

        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            board[r][c] = 'T'

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    dfs(nr, nc)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)

            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)

            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


        