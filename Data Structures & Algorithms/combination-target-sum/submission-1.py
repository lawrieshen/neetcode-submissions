class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, current_sum):
            if current_sum >= target:
                if current_sum == target:
                    result.append(path[:])
                else:
                    return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, current_sum + nums[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result
