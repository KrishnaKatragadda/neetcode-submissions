class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ## when we need to figure out what intervals satisfies a condition
        ## we can translate the problem into saying
        ## certain intervals are active (valid for condition), find the required

        intervals.sort(key = lambda i:i[0]) ## sorting the interval by start
        ## we need to store the indices of the query elements in the query
        minHeap =[]
        i=0
        ans = [-1]*len(queries)
        sorted_queries = sorted((q,i) for i,q in enumerate(queries))

        for q in sorted_queries:
            while i <len(intervals) and intervals[i][0]<=q[0]:
                 ## when start is less than query, it is active interval
                 ## this intervals needs to be added to minheap
                 l,r = intervals[i]
                 heapq.heappush(minHeap,(r-l+1,r))
                 i+=1
            ## adding all active intervals for the particular query is completed
            ## now we need to add the minimum length interval to the result list and 
            ## remove any inactive intervals from the minheap
            while minHeap and minHeap[0][1]<q[0]:
                heapq.heappop(minHeap) ## remove inactive intervals
            
            if minHeap:
                ans[q[1]] = minHeap[0][0]
        return ans
            

        