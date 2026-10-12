class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i +1
            r = len(nums) -1 
            target = -nums[i]

            while l<r:
                s = nums[l] + nums[r]

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r],nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
        return res