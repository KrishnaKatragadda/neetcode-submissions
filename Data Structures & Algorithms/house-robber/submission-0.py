class Solution:
    def rob(self, nums: List[int]) -> int:
        ## this is a DP problem
        ## the idea is to maximise rob money
        ## you need to make a decision of should i rob this house or skip
        ## we are worried about money we can loot

        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp= [0]*n ## this array to store the max amount rob till that house,including

        dp[0] = nums[0] ## max amount at house 0 is amount at that house
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        

        return dp[-1]
        