class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        look_up = {}
        for i, num in enumerate(nums):
            if num in look_up:
                if abs(i - look_up[num]) <= k:
                    return True
            
            look_up[num] = i

        return False