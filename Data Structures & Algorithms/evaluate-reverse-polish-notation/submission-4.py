class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = set(["+", "-", "*", "/"])

        stack = deque()

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()

                if token == "+":
                    stack.append((x + y))
                elif token == "-":
                    stack.append((x - y))
                elif token == "*":
                    stack.append((x * y))
                elif token == "/":
                    stack.append(int(x / y))
        
        return stack[0]