class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in range(9):
            cache = set()
            for j in range(9):
                if board[i][j] in cache:
                    return False
                if board[i][j] != ".":
                    cache.add(board[i][j])

        # check cols
        for j in range(9):
            cache = set()
            for i in range(9):
                if board[i][j] in cache:
                    return False
                if board[i][j] != ".":
                    cache.add(board[i][j])
        # check sub-boxes
        origins = [(0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6)
        ]

        for x, y in origins:
            cache = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] in cache:
                        return False
                    if board[i][j] != ".":
                        cache.add(board[i][j])

        return True
            
