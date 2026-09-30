class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ## this is a DP problem of 2D
        ## 0/1 knapsack problem structure

        ## step1: define a 2D matrix with zeros values as base

        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]

        ## there is one way to make a amount 0, by not making a choice
        for i in range(len(coins)+1):
            dp[i][0] =1
        
        for i in range(1,len(coins)+1):
            coin = coins[i-1]
            for j in range(1,amount+1):

                ## if you dont use the current coin
                dp[i][j] +=dp[i-1][j] 

                ## if you consider the current coin
                if j>= coin:
                    dp[i][j]+=dp[i][j-coin]
        
        return dp[len(coins)][amount]