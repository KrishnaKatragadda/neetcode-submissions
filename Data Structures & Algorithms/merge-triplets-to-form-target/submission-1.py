class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ## the key is that you can skip applying the transformation
        ## you dont need to consider applying them in order as well
        good = set()

        ## case1: we need to ignore any triplets that have values greater than
        ## target position at any index right, that will always grow
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue ## bad or big value than target
            
            for i,v in enumerate(t):
                if v==target[i]: ## if the value is equal to target
                    good.add(i) ## this index will contribute to solution
        
        return len(good)>=3
            
