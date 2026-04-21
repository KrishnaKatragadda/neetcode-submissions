class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 1 if len(nums)>0 else 0

        for n in nums:
            flag = True
            local = 1
            temp = n
            while flag:

                if temp+1 in nums:
                    temp = temp+1
                    local = local+1
                else:
                    flag = False
            maxL = max(maxL, local)

        return maxL              
        