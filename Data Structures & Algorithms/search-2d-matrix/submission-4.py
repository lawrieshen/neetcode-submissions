class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row_idx = -1
        left, right = 0, m - 1
        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if matrix[mid][0] == target or matrix[mid][-1] == target:
                    return True
                row_idx = mid
                break
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        if row_idx == -1:
            return False

        left = 1
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2

            if matrix[row_idx][mid] == target:
                return True
            elif matrix[row_idx][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False