class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)] # dp := can s[i:j] be a plaindrome or not
        # transition: dp[i][j] = dp[i + 1][j - 1] iff s[i] == s[j]
        # base case: can narrow to insepct dp[i + 1][j - 1]
        # a True i = 3, j = 3 s[i] == s[j]
        # aa True i = 3, j = 4 s[i] == s[j]
        # ab False i = 3, j = 4 s[i]
        # we need to speically handle cases when j - i < 2

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]