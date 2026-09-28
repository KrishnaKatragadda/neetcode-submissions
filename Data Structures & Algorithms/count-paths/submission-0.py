class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## This is a DP problem, at every point you need to calculate the sub-problem to get to it.

        ## Bottom-up iterative solution

        ## define a 2D array of size target_size+1

        dp = [[0]*(n+1) for _ in range(m+1)]

        ## define the base condition
        ## the last cell, if we start at that you have 1 way to reach to that
        dp[m-1][n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):

                ## at every point the number of ways to reach the last point
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
                print(dp[i][j])
        
        return dp[0][0]