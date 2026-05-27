class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        cache = []

        def checkPalindrome(s: str) -> bool:
            if not s:
                return False

            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if checkPalindrome(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result