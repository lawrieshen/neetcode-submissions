class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        def backtrack(x, y, index):
            if index == len(word):
                return True

            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[index]:
                return False

            char = board[x][y] 
            board[x][y] = "#" # Mark visited

            # Explore neighbors
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if backtrack(nx, ny, index + 1):
                        return True
            
            # restore
            board[x][y] = char

            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False