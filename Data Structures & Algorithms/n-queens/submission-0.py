class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def backtrack(row, cols, diagonal1, diagonal2, current_board):

            if row == n:
                result.append(["".join(row) for row in current_board])
                return

            for col in range(n):
                if col in cols or (row - col) in diagonal1 or (row + col) in diagonal2:
                    continue

                # place the queen
                current_board[row][col] = 'Q'
                cols.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                # next level
                backtrack(row + 1, cols, diagonal1, diagonal2, current_board)

                # restore
                current_board[row][col] = '.'
                cols.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        initial_board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), initial_board)

        return result