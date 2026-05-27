class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # A star
        start = '0000'
        queue = deque([(start, 0)])
        tried = {start}
        dead = set(deadends)

        if start in dead:
            return -1

        if start == target:
            return 0

        def attempts(code:str) -> List[str]:
            codes = []
            for i in range(4):
                digit = code[i]
                for move in (-1, 1):
                    new_digit = (int(digit) + move) % 10
                    codes.append(code[:i] + str(new_digit) + code[i + 1:])
            return codes

        while queue:
            code, step_count = queue.popleft()
            
            if code == target:
                return step_count

            for attempt in attempts(code):
                if attempt in dead or attempt in tried:
                    continue
                tried.add(attempt)
                queue.append((attempt, step_count + 1))


        return -1

        