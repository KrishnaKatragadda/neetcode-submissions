import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        sum = 0
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)

        while k>0:
            temp = math.isqrt(-1*heapq.heappop(maxHeap))
            heapq.heappush(maxHeap,-temp)
            k-=1
        
        for i in range(len(maxHeap)):
            sum+=-1*maxHeap[i]
        
        return sum

        