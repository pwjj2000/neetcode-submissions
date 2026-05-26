class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far, max_profit = prices[-1], 0
        for i in reversed(range(len(prices) - 1)):
            max_profit = max(max_profit, max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
        return max_profit