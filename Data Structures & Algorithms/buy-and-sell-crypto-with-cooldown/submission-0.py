class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = float('-inf')
        sold = 0
        rest = 0

        for price in prices:
            prev_sold = sold
            hold = max(hold, rest - price) # keep holding or sell
            sold = hold + price
            rest = max(rest, prev_sold) # cooldown state

        return max(sold, rest)