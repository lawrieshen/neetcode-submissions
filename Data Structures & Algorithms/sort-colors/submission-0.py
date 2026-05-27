class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = Counter(nums)

        i = 0
        for j in range(3):
            while counter[j] > 0:
                nums[i] = j
                i += 1
                counter[j] -= 1