class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## This is DP.
        ## i dont need to calculate everything
        ## i just need to see, if my next position gives me success. 

        ## I will use bottom up appraoch]
        # n = len(nums)
        # res = [False] * n
        # res[n-1] = True ## I'm assuming that the last position is a succss

        # for i in range(n-2,0,-1):
        #     res[i] = res[i+res[i]]
        # print(res)
        # return res[0]
        goal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal = i
        
        return True if goal == 0 else False
        