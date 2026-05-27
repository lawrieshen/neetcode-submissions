class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # dp[a] = min coins to make amount a
        dp[0] = 0
        # transition dp[a] = min(dp[a], using a new coin + the remaining problem)

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != float('inf') else -1

