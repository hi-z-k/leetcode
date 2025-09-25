class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bestSell = prices[0]
        for price in prices:
            bestSell = min(bestSell,price)
            profit = max(profit,price-bestSell)
        return profit