class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in range(9):
            cache = set()
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell not in cache:
                    cache.add(cell)
                else:
                    return False

        # check cols
        for col in range(9):
            cache = set()
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell not in cache:
                    cache.add(cell)
                else:
                    return False

        # check subboxes
        for row in range(3):
            for col in range(3):
                origin_row = row * 3
                origin_col = col * 3
                cache = set()
                for sub_row in range(origin_row, origin_row + 3):
                    for sub_col in range(origin_col, origin_col + 3):
                        cell = board[sub_row][sub_col]
                        if cell == ".":
                            continue
                        if cell not in cache:
                            cache.add(cell)
                        else:
                            return False
        
        return True
