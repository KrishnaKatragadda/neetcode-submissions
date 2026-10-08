class Solution:
    def isHappy(self, n: int) -> bool:
        ## so basically it is a cycle detection problem.

        visit = set()

        while n not in visit:
             ## Here we check if number is already visited
            visit.add(n)
            n = self.getSum(n)

            if n ==1:
                return True
        return False
    
    def getSum(self, m):
        output = 0

        while m:
            digit = m%10
            digit = digit**2
            output+=digit

            m = m//10
        
        return output


        