class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # definition of pivot point: nums[k] < nums[k - 1]
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # if left half is all sorted we can search here
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # if target is outside of the range of right half, we narrow toward the left
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1