class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap)>1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x==y:
                pass
            elif x<y:
                temp = y-x
                heapq.heappush(max_heap,-temp)
            else:
                temp= x-y
                heapq.heappush(max_heap,-temp)
        
        return -heapq.heappop(max_heap) if len(max_heap)>0 else 0
        