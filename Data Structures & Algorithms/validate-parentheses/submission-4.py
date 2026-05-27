class Solution:
    def isValid(self, s: str) -> bool:
        reference = {
            ')':'(',
            '}':'{',
            ']':'['
            }

        stack = deque()

        for c in s:

            if c in reference:
                if not stack or stack.pop() != reference[c]:
                    return False
            else:
                stack.append(c)

        return True if not stack else False