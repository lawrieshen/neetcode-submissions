class FreqStack:

    def __init__(self):
        self.counter = {} # {val: freq}
        self.group = {} # {freq : [val]}
        self.max_freq = float('-inf')

    def push(self, val: int) -> None:
        if val not in self.counter:
            self.counter[val] = 1
        else:
            self.counter[val] += 1

        if self.counter[val] not in self.group:
            self.group[self.counter[val]] = []

        self.group[self.counter[val]].append(val)

        self.max_freq = max(self.max_freq, self.counter[val])
    def pop(self) -> int:
        pop = self.group[self.max_freq].pop()
        self.counter[pop] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return pop

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()