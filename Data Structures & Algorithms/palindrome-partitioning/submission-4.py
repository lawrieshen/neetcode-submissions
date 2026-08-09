class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(start, end):
            if end >= len(s):
                if start == end:
                    res.append(part.copy())
                return

            # Check if s[start: end + 1] is a palindrome
            if self.isPali(s, start, end):
                part.append(s[start:end + 1])
                dfs(end + 1, end + 1) # move start to the next unpartitioned index
                part.pop()

            dfs(start, end + 1)

        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True