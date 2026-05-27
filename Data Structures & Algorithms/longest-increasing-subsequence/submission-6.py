from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tails = []
        for x in nums:
            i = bisect_left(tails, x)  # for strictly increasing
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
