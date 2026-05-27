class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # to help skipping diplicates

        def backtrack(start, path, current_sum):

            # base case
            if current_sum >= target:
                if current_sum == target:
                    result.append(path[:])
                else:
                    return

            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, current_sum + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result
                