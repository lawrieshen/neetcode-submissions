class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # binary search rows
        row_index = -1
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if matrix[mid][0] == target:
                    return True
                else:
                    row_index = mid
            
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if row_index == -1:
            return False

        # binary search cols
        left, right = 0, n - 1
        while left <= right:
            mid  = (left + right) // 2

            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        

        return False
