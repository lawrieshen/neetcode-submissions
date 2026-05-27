class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        count = 0 
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                
                # we want to check wether dp[i][j] (s[i:j+1] is palindromic or not)
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]): # i= 3, j = 3; i = 3, j = 4
                    dp[i][j] = True 
                    count += 1

        return count
        