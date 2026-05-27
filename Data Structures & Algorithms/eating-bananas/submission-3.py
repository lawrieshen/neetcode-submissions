class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            time = 0
            for p in piles:
                time += (p + speed - 1) // speed

            return True if time <= h else False
        
        upper_bound = max(piles)

        left = 1
        right = upper_bound

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left