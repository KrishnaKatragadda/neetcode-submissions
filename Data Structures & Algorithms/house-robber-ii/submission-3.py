class Solution:
    def rob(self, nums: List[int]) -> int:

        ## the idea is to run helper function two times
        ## we can skip the first element, then the remaining array is a normalset of house
        ## we can skip the last element, then they are not in circle any more
        ## if the array has only one element, then the calls will be on empty arrays
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))

    
    def helper(self, nums):

        n = len(nums)
        if n ==0: return 0
        if n ==1: return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]
        