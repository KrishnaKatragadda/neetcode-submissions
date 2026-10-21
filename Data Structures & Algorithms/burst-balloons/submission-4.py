class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## this is a trciky DP problem.

        ## it is given that if the index goes out of bound we need consider it as 1
        ## so we will add them

        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)] ## this stores the maximum coins we can get from bursting ballons between dp[l][r] will store max coins we can get within l,r
        
        ## iterative dp to avoid recursion overhead
        for length in range(1, n - 1): ## Number of ballons considered in subarray
            for l in range(1, n - length): ## goes and generates all possible subarray
                r = l + length - 1
                for i in range(l, r + 1): ## in the given subarray, find what if this gets burst last
                    coins = nums[l - 1] * nums[i] * nums[r + 1] + dp[l][i - 1] + dp[i + 1][r]
                    if coins > dp[l][r]:
                        dp[l][r] = coins

        return dp[1][n - 2]
        return dfs(1,len(nums)-2)