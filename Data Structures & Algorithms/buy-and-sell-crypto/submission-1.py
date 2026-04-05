class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 101

        for price in prices:
            if price > min_price:
                profit = max(price-min_price, profit)
            else:
                min_price = price

        return profit
