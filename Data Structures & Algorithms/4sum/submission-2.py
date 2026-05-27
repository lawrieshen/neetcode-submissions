class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # for K > 2, we fix one element and recursively solve (K - 1)-Sum.
        # when K reaches 2, we use the two-pointer approach as the base case

        # step 1: sort the array

        # step 2: define recursive function kSum(k, start, target)

            # base case: k == 2 -> user two pointers from start to find pairs summing to target

            # recursive case: for each element at index 1 from start, recursively call kSum(k - 1, i + 1, target - nums[i])

            # skip duplicates at each recursive level

            # track the current partial solution in a list, adding/removing elements as we recurse


        # step 3 call kSum(4, 0, target) and return the collected results

        nums.sort()

        res, cache = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(cache + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[l] == nums[r + 1]:
                            r -= 1
                
                return 

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cache.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                cache.pop()

        kSum(4, 0, target)
        return res