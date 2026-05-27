class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        length = total // k
        subsets = [0] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True
            
            for idx in range(k):
                if subsets[idx] + nums[i] <= length:
                    subsets[idx] += nums[i]
                    if dfs(i + 1):
                        return True
                    subsets[idx] -= nums[i]

                if subsets[idx] == 0:
                    break

            return False

        return dfs(0)