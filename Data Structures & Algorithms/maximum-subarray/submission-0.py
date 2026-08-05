class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            if currSum <0: ## when ever the resultant sum of elements untill 
            ## the point results in value which is less than 0, ignore the 
            ## prefix elements
                currSum = 0
            currSum+=n
            maxSum = max(currSum, maxSum)
        
        return maxSum
        