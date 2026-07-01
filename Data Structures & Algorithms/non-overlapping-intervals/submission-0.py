class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ## We need to sort first, 
        ## it is asking for NON-OVERLAPPING--> sort by end
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i[1])

        temp = intervals[0]
        count = 0
        for start,end in intervals[1:]:
            if temp[1] > start:
                count+=1
            else:
                temp = [start,end]
        
        return count

        