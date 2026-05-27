class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # find left most smallest boundaries
        left_most_smallest = [-1] * n
        stack = deque()
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_most_smallest[i] = stack[-1]
            stack.append(i)

        # find right most smallest boundaries
        right_most_smallest = [n] * n
        stack.clear()
        for j in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                right_most_smallest[j] = stack[-1]
            stack.append(j)
             
        # calculate area and return the max
        max_area = 0
        for k in range(n):
            area = heights[k] * ((right_most_smallest[k] - 1) - (left_most_smallest[k] + 1) + 1)
            max_area = max(max_area, area)

        return max_area
            