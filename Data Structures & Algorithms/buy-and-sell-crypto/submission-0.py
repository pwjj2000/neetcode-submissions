class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in reversed(range(len(prices) - 1)):
            max_profit = max(max_profit, prices[i + 1] - prices[i])
            prices[i] = max(prices[i], prices[i + 1])
        return max_profit