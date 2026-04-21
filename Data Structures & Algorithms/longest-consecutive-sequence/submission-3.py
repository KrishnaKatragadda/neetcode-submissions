class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 1 if len(nums)>0 else 0
        numSet = set(nums)


        for n in nums:
            ## check if n is the starting of a sequence
            if n-1 not in numSet:
                curr = n
                local = 1
                while curr+1 in numSet:
                    curr = curr+1
                    local = local+1
                maxL = max(maxL,local)
        
        return maxL
        # maxL = 1 if len(nums)>0 else 0

        # for n in nums: ## as we are trying to find an element in list.. it loops through 
        # ## all the elements in the list. O(n). 

        # ## instead, if we convert it to set. THe lookup will just be O(1)
        #     flag = True
        #     local = 1
        #     temp = n
        #     while flag: ## also i'm running the while loop for all the elements,
        #     ## it is not necessary

        #         if temp+1 in nums:
        #             temp = temp+1
        #             local = local+1
        #         else:
        #             flag = False
        #     maxL = max(maxL, local)

        # return maxL              
### This solution works, BUT it is not optimal. It is brute force
