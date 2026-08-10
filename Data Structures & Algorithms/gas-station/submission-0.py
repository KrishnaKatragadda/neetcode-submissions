class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ## This is tricky irritating
        ## Base condition is
        ## total global available gas should be sufficient to the 
        ## cost of the entire road, trip then a solution exists

        if sum(gas)< sum(cost):
            return -1
        
        ## if the above block doesn't run, then a solution is present
        total = 0 ## this gives the gas in the tank
        res = 0## tracks the position of success
        for i in range(len(gas)):
            total+= gas[i]-cost[i]

            if total < 0: ## any position where the you are negative
                total = 0
                res = i+1 ## lets hope the next position gives success
            
        
        return res
        