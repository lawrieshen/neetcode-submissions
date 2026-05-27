class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)

        # result = [0] * n

        # stack = deque()

        # # monotonically decreasing
        # for i, t in enumerate(temperatures):
        #     while stack and stack[-1][0] < t:
        #         temp, index = stack.pop()
        #         result[index] = i - index
                
        #     stack.append((t, i))
        
        # return result 
        n = len(temperatures)

        result = [0] * n

        stack = deque()

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((t, i))

        return result