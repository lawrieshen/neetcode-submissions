class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1) # dp[i] is the ways we can decode the prefix s[:i] and we want dp[n] at the end
        # dp[0] = 1
        # dp[1] = 1 if s[0] != '0' else 0

        dp0 = 1
        dp1 = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            # dp[i] += (dp[i-1] if s[i-1] != '0' else 0) # one digit
            #         + (dp[i-2] if (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] in '0123456')) else 0) # two digit
            cur = 0
            if s[i-1] != '0':
                cur += dp1
            
            if (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] in '0123456')):
                cur += dp0

            dp0, dp1 = dp1, cur

        return dp1