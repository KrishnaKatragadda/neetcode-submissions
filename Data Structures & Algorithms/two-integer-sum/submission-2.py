class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = {}

        for i in range(len(nums)):

            soft_target = target-nums[i]
            if soft_target in dict1: return [dict1[soft_target],i]
            dict1[nums[i]] = i