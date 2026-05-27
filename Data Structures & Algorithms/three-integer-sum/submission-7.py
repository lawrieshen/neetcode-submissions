class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointer
            j, k = i + 1, n - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]

                if summ == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif summ < 0:
                    j += 1
                else:
                    k -= 1

        return res

                

