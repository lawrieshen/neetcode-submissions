class MinStack:

    def __init__(self):
        self.min = float('inf') # stores the current minimum in the stack
        self.stack = [] # stores encoded values
        # each value is encoded relative to the min at the time it was pushed, and we can reverse it correctly during pop

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0 : # this value created a new minimum at the time it got pushed onto the stack
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
