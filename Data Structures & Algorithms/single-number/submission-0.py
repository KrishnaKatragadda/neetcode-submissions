class Solution:
    def singleNumber(self, nums: List[int]) -> int:
### XOR operation on same number gives 0
### n XOR 0 is n
        res = 0
        for i in nums:
            res = res ^ i
        
        return res