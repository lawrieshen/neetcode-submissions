class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        res = 1

        self.stocks.append(price)

        i = len(self.stocks) - 1
        while i > 0 and price >= self.stocks[i - 1]:
            res += 1
            i -= 1
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)