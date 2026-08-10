class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        ## create a min Heap to store the all elements with the frequencies
        if len(hand) % groupSize:
            return False
        count = {}
        for i in hand:
            count[i] = count.get(i,0)+1
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
                