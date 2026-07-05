class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count ={} ## dictionary to store the count of freq
        ## we are iterating elements in list from left to right,
        ## so index condition of i<j always holds
        for n in nums:
            if n in count: ## lets say, we are seeing 1 at index 3, we found 1 at inde
            ## 0, we can form a pair with (0,3)--2, next for 1 at index 4,
            ## (0,4),(0,3),(3,4) -- 3
                res+= count[n]
                count[n]+=1
            else:
                count[n] =1
        
        return res


        