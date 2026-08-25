class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lower = prices[0]

        for i in range(len(prices)):
            if prices[i] < lower:
                lower = prices[i]
            profit = max(profit, prices[i] - lower)

        return profit