class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(x, y, index):
            if index == len(word):
                return True

            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[index]:
                return False

            temp, board[x][y] = board[x][y], "#"

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if backtrack(nx, ny, index + 1):
                    return True

            # backtrack step
            board[x][y] = temp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False