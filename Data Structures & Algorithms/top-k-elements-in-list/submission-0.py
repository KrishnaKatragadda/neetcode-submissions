class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## For finding the frequency of elements, using dictionary is key
        freqDict = {}
        for n in nums:
            freqDict[n] = 1+ freqDict.get(n,0)

        ## construct a min-heap in accordance with freq order
        heap = []
        for num in freqDict.keys():
            heapq.heappush(heap, (freqDict[num],num))
            if len(heap)>k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res       