class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        points = 0
        
        for operation in operations:
            if operation == "+":
                if len(stack) >= 2:
                    points += stack[-1] + stack[-2]
                    stack.append(stack[-1] + stack[-2])

            elif operation == "D":
                points += stack[-1] * 2
                stack.append(stack[-1] * 2)

            elif operation == "C":
                points -= stack.pop()
            
            else:
                points += int(operation)
                stack.append(int(operation))

        return points

