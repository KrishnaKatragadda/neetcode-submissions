class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## when you buy, increase the index by 1, i+1
        ## when you sell, increase the index by 2, i+2 because of manditory cooldown

        dp = {} ## key is (index, buying or selling) stores the max profit you can get by that combination

        def dfs(i,buying):
            ## base condition

            if i>= len(prices): return 0

            ## check if the combination is already calculates
            if (i,buying) in dp: return dp[(i,buying)]
            ## you need to check what will you get if you choose cooldown
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2, not buying)+ prices[i]
                dp[(i,buying)] = max(sell, cooldown)
            
            return dp[(i,buying)]
        
        return dfs(0,True)
        