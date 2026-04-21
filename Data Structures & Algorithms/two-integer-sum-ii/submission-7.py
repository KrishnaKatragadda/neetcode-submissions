class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        ## As it is a sorted array and we can check against a condition
        ## we can use two pointer approach
        while left< right:
            if numbers[left]+numbers[right]>target: 
                ## If sum of elements is more than target, we need get the sum down
                right-=1
            elif numbers[left]+numbers[right]<target:
                ## If sum is less than target, we need to increase it
                left+=1
            else:
                return [left+1, right+1]

        