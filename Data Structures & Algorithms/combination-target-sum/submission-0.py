class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, sol, current_sum):
            if current_sum == target:
                result.append(sol[:])
            elif current_sum> target:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(i, sol, current_sum + nums[i])
                sol.pop()

        backtrack(0, [], 0)
        return result