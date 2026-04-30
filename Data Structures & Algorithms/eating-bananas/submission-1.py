class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        ## the condition is the, number of hours available is
        ## always greater than the number of available piles

        ## So, if we get the max(piles) as rate, we will for sure be able
        ## to eat the bananas. But we need to find the minimum right, k =1

        left = 1
        right = max(piles) ## doing a binary search in the possible rates
        rate = right

        while left<=right:
            hours = 0
            mid = (left+right)//2

            for p in piles:
                hours+= math.ceil(p/mid) ## calculating the time at this rate
            
            if hours<= h: ## if within the limit
                right = mid-1
                rate = min(rate, mid)
            else:
                left = mid+1 

        return rate
        