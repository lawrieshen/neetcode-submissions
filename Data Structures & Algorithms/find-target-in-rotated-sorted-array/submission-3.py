class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pass: find pivot point first, then search on the side where target at

        # one pass
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]: # left half is sorted, then we want to use it to search
                # if target is within the left half, we narrow down into this range
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                # we focus on the right half of the searching range
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
                      