class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## this is a DP problem.
        ## Lets say, you are at last step, for you to cross the index
        ## min cost is cost to step+0
        n = len(cost)
        dp = [0]*(n+1)

        dp[n-1] = cost[n-1]

        for i in range(n-2,-1,-1):
            dp[i] = cost[i]+min(dp[i+1],dp[i+2])

        return min(dp[0],dp[1])