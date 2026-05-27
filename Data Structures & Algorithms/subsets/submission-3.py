class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subsets):
            res.append(subsets[:])

            for j in range(i, len(nums)):
                subsets.append(nums[j])
                backtrack(j + 1, subsets)
                subsets.pop()

        backtrack(0, [])

        return res

            