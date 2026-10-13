class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)):
            l = i
            r = l+1
            while r < len(prices):
                if prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    res = max(res,profit)
                r+=1
        return res 

        