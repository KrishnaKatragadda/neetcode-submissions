class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        ## phase 1: cycle detection. Break the cycle after detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
            
        
        ## phase 2: reset the pointer to start and move both pointer by 1 step
        ## the point they meet, it is the starting point of loop and duplicate

        slow = nums[0]

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        