class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        current_board = [['.' for _ in range(n)] for _ in range(n)]

        def dfs(row, cols, diag1, diag2):
            if row == n:
                result.append(["".join(row) for row in current_board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # palce the queen
                current_board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # next row
                dfs(row + 1, cols, diag1, diag2)

                #restore
                current_board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        dfs(0, set(), set(), set())
        return result