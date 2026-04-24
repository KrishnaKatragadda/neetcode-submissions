class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        ## basic idea of making profit is
        ## buy at the lowest and sell at the highest

        ## to identify lowest, find the lowest from left to right.
        ## Keep comparing profit against the lowest.

        for i in range(len(prices)):
            lowest = min(lowest,prices[i])
            if prices[i]-lowest >0:
                profit = max(profit,prices[i]-lowest)
        return profit
        