class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # flip all the 'O' not connected to boarder to X

        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # use dfs to temporatily mark cells connected to boarder as 'T
        def dfs(x, y):
            # base case
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != 'O':
                return

            # process the cell
            board[x][y] = 'T'
            
            # explore the neighbor
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = dx + x, dy + y
                dfs(nx, ny)

        for i in range(m):
            if (board[i][0] == 'O'):
                dfs(i, 0)
            
            if (board[i][n - 1] == 'O'):
                dfs(i, n - 1)
            
        for j in range(n):
            if (board[0][j] == 'O'):
                dfs(0, j)

            if (board[m - 1][j] == 'O'):
                dfs(m - 1, j)

        # flip all 'O' to 'X' and all 'T' to 'O'
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif (board[i][j] == 'T'):
                    board[i][j] = 'O'