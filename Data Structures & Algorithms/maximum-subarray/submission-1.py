class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]
        for i in nums[1:]:
            current = max(i,current + i)
            best = max(best,current)
        return best 