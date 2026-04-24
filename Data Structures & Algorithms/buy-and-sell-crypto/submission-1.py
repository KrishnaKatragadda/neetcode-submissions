class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for i in range(len(prices)):
            lowest = min(lowest,prices[i])
            if prices[i]-lowest >0:
                profit = max(profit,prices[i]-lowest)
        return profit
        