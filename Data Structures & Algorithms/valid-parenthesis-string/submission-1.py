class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0
## this is a problem where the occurance of * can be (,) or empty 
## so at every step we can have a possibility of range of values 
## case 1: if it is straight for (, number of opens is +1
        for c in s:
            if c=="(": ## case 1: if it is straight for (, number of opens is +1
                minOpen+=1
                maxOpen+=1
            elif c ==")": ## case 2: if it is straight for ), number of opens is -1 because the existing opens will be negated by closed 
                minOpen-=1
                maxOpen-=1
            else: ## if it is * then we have a range of possibilities
                minOpen-=1
                maxOpen+=1
            
            if maxOpen <0: ## if at any point the maxOpens becomes -ve then False
                return False
            if minOpen<0: ## if the min is negative, we need to make it 0
            ## there can be case where they string is just * or ***
            ## then we will decrement
                minOpen = 0
        
        return minOpen ==0

        