class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            if total_time <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        
        return result