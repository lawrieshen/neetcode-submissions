class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))


        return stack[0]
            