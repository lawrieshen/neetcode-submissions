class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        n = len(s)
        res = []
        path = []


        def dfs(i):
            if i >= len(s):
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if isPali(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1

            return True

        dfs(0)
        return res
