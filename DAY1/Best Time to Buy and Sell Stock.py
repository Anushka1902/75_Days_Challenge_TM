class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if low<prices[i]:
                profit=max(profit, prices[i]-low)
            else:
                low = prices[i]
        return profit
