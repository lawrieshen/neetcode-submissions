class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right: # if left == right, we find the pivot point, don't need to search
            mid = (left + right) // 2

            if nums[mid] > nums[right]: # pivot point is in the right hand side
                left = mid + 1
            else: # pivot point is in the left hand side while still could be the cursor itself
                right = mid

        return nums[left] # or right

                