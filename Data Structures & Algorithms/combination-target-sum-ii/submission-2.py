class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, currSum):
            if currSum > target:
                return
            if currSum == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, currSum + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res