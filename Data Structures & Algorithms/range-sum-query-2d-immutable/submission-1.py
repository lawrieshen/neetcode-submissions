class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            row_running = 0
            for c in range(n):
                row_running += matrix[r][c]
                self.prefix_sum[r + 1][c + 1] = self.prefix_sum[r][c + 1] + row_running

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ps = self.prefix_sum
        return (
            ps[row2+1][col2+1]
            -ps[row1][col2+1]
            -ps[row2+1][col1]
            +ps[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)