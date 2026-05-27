class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # O(N log N)

        def backtrack(start, path): # O(2^N)
            result.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i]) # O(N)
                backtrack(i + 1, path)
                path.pop() # O(N)

        backtrack(0, [])

        return result

        # Time Complexity: O(N Log N + 2^N * N) = O(2^N * N) since O(2^N) grows exponentially
        # Space Complexity: O(2^N * N) The result array stores all unique subsets O(2^N) and each subset can contain up to N nums