class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        maxArea = 0
        
        l, r = 0, n - 1

        while l < r:
            area = min(heights[l], heights[r]) * abs(l - r)
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea