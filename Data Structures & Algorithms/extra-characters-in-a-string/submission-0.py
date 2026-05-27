class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # At each index in s, what is the minimum number of extra characters from here to the end?

        # try to match a dictionary word starting at position i
        # if you can match one, jump to the end of that word
        # if you cannot or choose not to use one, treat s[i] as an extra character and move to i + 1

        if not s:
            return 0

        if not dictionary:
            return len(s)

        n = len(s)

        words = set(dictionary) # use tri instead later

        dp = [0] * (n + 1) # dp[i] define min characters starting from index; at the end we want dp[0]

        # for i from n - 1 down to 0
            # set dp[i] = 1 + dp[i + 1]
            # for each word in the dictionary:
                # if i + len(word) <= n and s[i:i + len(word)], update dp[i] = min(dp[i], dp[i + len(word)])

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for word in dictionary:
                if i + len(word) <= n and s[i:i + len(word)] == word:
                    dp[i] = min(dp[i], dp[i + len(word)])

        return dp[0]
