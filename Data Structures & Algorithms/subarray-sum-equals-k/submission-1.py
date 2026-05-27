class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currentSum = 0
        prefixSums = { 0: 1}

        for num in nums:
            currentSum += num
            diff = currentSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)

        return res
