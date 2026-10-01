class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, s):
            
            if i ==len(nums):
                if s==target: return 1
                else: return 0
            
            if (i,s) in cache: return cache[(i,s)]

            cache[(i,s)] = dfs(i+1,s+nums[i]) + dfs(i+1, s-nums[i])

            return cache[(i,s)]
        
        return dfs(0,0)


            
