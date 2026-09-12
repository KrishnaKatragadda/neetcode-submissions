class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## consider the number at last index of the list,
        ## the maximum longest increasing subsequence is always one right

        LIS = [1]*(len(nums))
        ## if lets say, decreaseing list like 5,4,3,2,1 then the LIS is always 1

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        

        return max(LIS)
        