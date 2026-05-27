class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board and not board[0] and not word:
            return False

        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def dfs(x, y, index):
            if index == len(word):
                return True

            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[index]:
                return False

            char = board[x][y]
            board[x][y] = '#'

            for direction in directions:
                dx, dy = direction
                if dfs(x + dx, y + dy, index + 1):
                    return True
            
            board[x][y] = char

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i , j, 0):
                    return True

        return False