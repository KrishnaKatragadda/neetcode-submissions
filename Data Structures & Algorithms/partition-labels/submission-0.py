class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ## we need to keep track of the last index of the element in the string
        lastIndex = {} 

        for i,v in enumerate(s):
            lastIndex[v] = i
        ## now we have the character and its last index in the string
        res = []
        size, end = 0,0
        for i, c in enumerate(s):
            size+=1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(size)
                size = 0

        return res