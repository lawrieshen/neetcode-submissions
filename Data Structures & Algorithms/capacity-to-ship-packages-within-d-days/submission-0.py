class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if not weights:
            return 0

        if days < 0:
            return -1

        def valid(capacity):
            days_used = 1
            current_loading = 0
            for w in weights:
                current_loading += w
                if current_loading > capacity:
                    days_used += 1
                    current_loading = w
            
            return True if days_used <= days else False

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2

            if valid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left