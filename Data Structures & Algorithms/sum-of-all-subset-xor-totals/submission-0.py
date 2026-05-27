class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtracking(i, subset):
            nonlocal res
            xorr = 0
            for num in subset:
                xorr ^= num
            res += xorr

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtracking(j + 1, subset)
                subset.pop()

        backtracking(0, [])

        return res