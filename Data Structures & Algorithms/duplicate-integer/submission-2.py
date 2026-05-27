class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        if len(counter) != len(nums):
            return True
        else:
            return False