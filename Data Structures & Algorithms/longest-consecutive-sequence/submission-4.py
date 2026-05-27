class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in cache: # this means this is a starting point of a sequence
                cursor = num
                length = 1
                while cursor + 1 in cache:
                    length += 1
                    cursor += 1
                longest = max(longest, length)
        
        return longest
