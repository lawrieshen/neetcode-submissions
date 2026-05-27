class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1

        row = -1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if matrix[mid][0] == target or matrix[mid][-1] == target:
                    return True
                else:
                    row = mid
                    break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        if row == -1:
            return False

        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False