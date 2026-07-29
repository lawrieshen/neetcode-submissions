class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in cache:
                cursor = num
                length = 1
                while cursor + 1 in cache:
                    cursor += 1
                    length += 1
                res = max(res, length)

        return res