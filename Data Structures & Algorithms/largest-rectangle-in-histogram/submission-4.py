class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack
        stack = deque()
        max_area = 0
        heights.append(0)
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - 1 - stack[-1]
                area = height * width
                max_area = max(max_area, area)            
            stack.append(i)

        return max_area
            