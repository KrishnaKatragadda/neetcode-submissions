class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap =[] ## to calculate the distance and store points
        res = []
        for i in points:
            d = (i[0])**2 + (i[1])**2
            min_heap.append([d,i[0],i[1]])
        
        heapq.heapify(min_heap)

        while k>0:
            d,x,y = heapq.heappop(min_heap)
            res.append([x,y])
            k-=1
        
        return res

            

        