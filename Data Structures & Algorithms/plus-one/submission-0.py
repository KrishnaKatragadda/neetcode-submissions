class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## I want to reverse the given array
        digits = digits[::-1]
        carry, i = 1,0

        while carry:

            if i < len(digits): ## the index is within range
                if digits[i]==9: ## If this is first element it will produce carry. If it is decimal in btw if there is a carry it will continue
                    digits[i]=0
                else:
                    digits[i]+=1
                    carry = 0
            else:
                digits.append(carry)
                carry = 0 ## we should set this, otherwise Infinite loop
            i+=1
        return digits[::-1]

        