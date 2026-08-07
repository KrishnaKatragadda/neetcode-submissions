class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 ## stores the number of jumps
        l = r = 0
        while r< len(nums)-1:
            farthest = 0 ## you want to see, from current position## what is the farthest you can jump## so from that position you can aim for target
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            ## now you have calculated the farthest you can jump with the current level
            l = r+1
            r = farthest
            res+=1
        
        return res
            