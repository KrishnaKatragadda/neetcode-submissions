class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        res = nums[0]

    ## There will be two sorted segments in the list.
    ## We need to identify which segment will have the min in them

        if nums[left]<nums[right]: ## check if the first element is less than last element
        ## then it is in not rotated state
            return nums[left]

        while left<=right:
            mid = (left+right)//2
            res = min(res, nums[mid])

            if nums[mid]< nums[right]:
                right = mid-1
            else:
                left = mid+1
        
        return res

        