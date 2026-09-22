class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ## check if the total sum of the array is even, if odd return False immediately
        n = len(nums)
        sum = 0
        for i in nums:
            sum+=i
        
        if sum %2 !=0: return False
        target = sum//2
        memo = {} ## we are calculating it many times same index and target value
        def dfs(i,target):

            if target ==0:
                return True
            
            if target<0 or i>=n:
                return False
            
            if (i,target) in memo:
                return memo[(i,target)]
            
            take = dfs(i+1, target-nums[i])
            skip = dfs(i+1,target)

            memo[(i,target)] = take or skip 
            return memo[(i,target)]
        
        return dfs(0,target)