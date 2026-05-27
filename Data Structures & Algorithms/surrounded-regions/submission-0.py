class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
            
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != 'O':
                return

            board[x][y] = 'T'
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x + dx, y + dy)

        # mark all 'O's connected to board with T
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

        # flip all of the 'O' to 'X' and all of the 'T' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'T':
                    board[i][j] = 'O' 