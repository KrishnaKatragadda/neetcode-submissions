class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        print(ans)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)]=nums[i]
        
        return ans
        