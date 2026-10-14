class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount = 0
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        
        return max(count,key = count.get)
        