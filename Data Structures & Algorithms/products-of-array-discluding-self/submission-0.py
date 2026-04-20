class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ## when dealing with sums, products of arrays
        ## applying prefix and suffix methods will help solve it
        prefix= [1]*n
        suffix = [1]*n
        output = [0]*n

        for i in range(n-1):
            prefix[i+1] = prefix[i]*nums[i] ## getting product of all refix without the element 
        
        for j in range(n-1,0,-1):
            suffix[j-1] = suffix[j]*nums[j] ## getting product of all suffix without the element at index
        
        for k in range(n):
            output[k]= prefix[k]*suffix[k] ## multiply both the arrays to get final outputs
        
        return output
        
        