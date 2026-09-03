class Solution:
    def climbStairs(self, n: int) -> int:
        ## this is a DP problem
        ## top down memoization approach

        if n<=2:
            return n

        dp = [0]*(n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]