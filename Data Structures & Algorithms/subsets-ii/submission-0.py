class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        nums.sort()

        def helper(cur):

            if cur >= len(nums): ## base condition
                res.append(subset.copy())
                return 
            
            subset.append(nums[cur]) ## choose
            helper(cur+1)

            while cur+1<len(nums) and nums[cur]==nums[cur+1]:
                cur+=1
            
            subset.pop()
            helper(cur+1)

        
        helper(0)
        return res
        