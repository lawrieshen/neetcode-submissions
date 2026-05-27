class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def partition(left, right):
            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = partition(left, right)

            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        return -1