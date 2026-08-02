class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def findBound(isFirst: bool) -> int:
            l, r = 0, len(nums) -1
            bound = -1
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    bound = mid
                    
                    if isFirst:
                        r = mid - 1
                    else:
                        l = mid + 1

                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return bound

        return [findBound(True), findBound(False)]