class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            ans = max(ans, profit)
            min_price = min(min_price, prices[i])

        return ans