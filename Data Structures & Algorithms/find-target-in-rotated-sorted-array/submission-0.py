class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## when dealing with binary seach, use left, right

        left = 0
        right = len(nums)-1

        while left <=right:
            mid = (left+right)//2

            if target == nums[mid]:
                return mid
            
            ## mid belongs to left sorted array
            if nums[left]<= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid+1
                else:
                    right = mid -1
            ## mid belongs to right sorted array
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid-1
                else:
                    left = mid+1
        return -1

        