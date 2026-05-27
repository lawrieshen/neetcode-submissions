class MinStack:

    def __init__(self):
        self.stack = [] # normal stack for top()
        self.min_stack = [] # store (val, count) to handle duplication; for getMin()
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        # monotonic increasing (always keeps the min one at last)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        target = self.stack.pop()

        if target == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
        
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1][0]
        
