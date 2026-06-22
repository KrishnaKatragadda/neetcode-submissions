class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter ={} ## to store the Tasks and their frequencies

        for t in tasks:
            counter[t] = 1+counter.get(t,0)
        
        maxHeap = [-f for f in counter.values()]
        heapq.heapify(maxHeap) ## constructing a maxHeap with frequencies

        q = deque() ## will store the remaining freq and time at which 
        time = 0
        while maxHeap or q:
            time+=1

            if maxHeap:
                freq = 1+ heapq.heappop(maxHeap)

                if freq: ## if there is still freq to process, add them to queue with availability
                    q.append((freq, time+n))
            
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
