class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ## This is a Graph problem, so we need to represent the given
        ## scenario as adjacency list

        edges = {} ## creating a adjacency list

        for i in range(1,n+1):
            edges[i] = []
        
        for u,v,t in times:
            edges[u].append((v,t))
        
        time = 0
        visit = set() ## to track if all the nodes in the graph are visited.
        minHeap = [(0,k)] ## strating from the seed node

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            time = max(time,w1)

            ## implementing the BFS part
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))
        return time if len(visit) == n else -1