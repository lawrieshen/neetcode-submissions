class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        lookup = {
            '1': '',
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': 'wxyz'
        }

        res = []
        path = []

        def dfs(start):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            for i in range(start, len(digits)):
                for c in lookup[digits[i]]:
                    path.append(c)
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return res
