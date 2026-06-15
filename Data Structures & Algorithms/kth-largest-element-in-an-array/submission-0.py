class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = [-i for i in nums]
        c = 0

        heapq.heapify(max_heap)

        while c<k:
            res = -heapq.heappop(max_heap)
            c+=1
        
        return res

