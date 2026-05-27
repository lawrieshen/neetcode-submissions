class Solution:
    def isValid(self, s: str) -> bool:
        references = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for c in s:
            if c in references:
                if not stack:
                    return False
                if references[c] != stack.pop():
                    return False

            else:
                stack.append(c)

        return not stack