from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        stack.append(nums[0])

        length = 1

        for i in range(1, len(nums)):
            if stack[-1] < nums[i]: # strictly increasing
                stack.append(nums[i])
                length += 1
                continue

            # if not increasing, replace the new smaller num with in the stack
            idx = bisect_left(stack, nums[i])
            stack[idx] = nums[i]

        return length
