class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # because the car can only form a fleet with another car thatis behind of it,
        # sorting the array in descending order ensures calirty about the final speed of each car
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)