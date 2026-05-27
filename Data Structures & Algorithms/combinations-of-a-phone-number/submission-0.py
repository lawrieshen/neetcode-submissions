class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        def backtrack(start, path):
            if start == len(digits):
                result.append("".join(path))
                return

            for letter in digit_to_letter[digits[start]]:
                path.append(letter)
                backtrack(start + 1, path)
                path.pop()

        backtrack(0, [])

        return result
