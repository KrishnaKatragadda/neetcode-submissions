class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = [] ## to hold the result set

        def dfs(i,curr,total):

            ##base condition1:
            if total == target:
                res.append(curr.copy())
                return
            
            ##base condition2:
            if i >= len(nums) or total > target:
                return
            

            ## decision to include present element
            curr.append(nums[i])
            dfs(i,curr,total+nums[i])

            ## decision to not include present element
            curr.pop()
            dfs(i+1, curr, total)

        
        dfs(0,[],0)
        return res
        