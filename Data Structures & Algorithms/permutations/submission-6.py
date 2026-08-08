class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in used:
                    continue
                
                used.add(num)
                path.append(num)
                backtrack(path)
                used.remove(num)
                path.pop()

        backtrack([])
        return res

        # Time: O(n * n!); n! nodes * n for each copy operation
        # Space: O(n) auxiliary, O(n * n!) including output