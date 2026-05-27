class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Binary search rows
        row_idx = -1
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if matrix[mid][0] == target or matrix[mid][-1] == target:
                    return True
                else:
                    row_idx = mid
                    break

            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        if row_idx == -1:
            return False

        # Binary search cols
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[row_idx][mid] == target:
                return True
            elif matrix[row_idx][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
