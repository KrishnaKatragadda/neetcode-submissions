class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}

        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     if amount in memo:
        #         return memo[amount]

        #     res = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))

        #     memo[amount] = res
        #     return res

        # minCoins = dfs(amount)
        # return -1 if minCoins >= 1e9 else minCoins

        dp = [amount+1]*(amount+1)

        dp[0] = 0 ## this is the base case, number of coins needed to get 0

        for i in range(1,amount+1):
            for c in coins:
                if (i-c)>=0: ## the amount we want to achieve after coin used is positive, we need to look for other coins
                    dp[i] = min(dp[i], 1+dp[i-c])
        
        return dp[amount] if dp[amount]!= amount+1 else -1