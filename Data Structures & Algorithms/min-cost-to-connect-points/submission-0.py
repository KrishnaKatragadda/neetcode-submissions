class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ##ok, This is a graph problem.
        ## First step is to build an adjacency list to represent the Graph
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            ## for every point calculate the distance for every other point in the graph
            for j in range(i+1,N):
                x2,y2 = points[j]
                distance = abs(x2-x1) + abs(y2-y1)

                adj[i].append([j,distance])
                adj[j].append([i,distance])

        minCost = 0
        visit = set()
        minH = [[0,0]] ## the reason we say 0,0 is- with Prims algorithm we can start at any point
        ## we will start at first point which is 0-- the cost to connect this is 0

        ### You can run the algorithm until minHeap is empty or visit length is equal to the number of nodes in the graph

        while len(visit)<N:
            ## pop of the minimum cost element from minH
            cost,dst = heapq.heappop(minH)

            ## check if the destination possible is already visited, this avoids the cycle
            if dst in visit:
                continue
            
            minCost+=cost
            visit.add(dst)

            ## now explore the new node
            for nei,cost2 in adj[dst]:
                if nei not in visit:
                    heapq.heappush(minH,[cost2,nei])
        return minCost
