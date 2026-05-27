class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # closest to the destination
        cars = sorted(zip(position, speed), reverse=True)

        stack = deque()

        for pos, spd in cars:
            time = (target - pos) / spd
            print(time)
            if not stack or time > stack[-1]: # if the time the care behind take is greater than the previous car than it's not in the smae fleet as the previous car
                stack.append(time)

        return len(stack)

        