class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        ## this is graph problem, so construct a adjacency list
        ## directed

        # adj = {i:[] for i in range(n)}

        # for s,d,c in flights:
        #     adj[s].append((d,c))
        # print(adj)

        prices = [float("inf")] * n ## we are declaring the cost to be Inf
        prices[src] =0 ## minimum cost to get to src.

        for i in range(k+1):
            ## we will be exploring all the edges k+1 times, as we are allowed
            ## k stops, so we will loop k+1
            tempPrices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s]+p < tempPrices[d]:
                    tempPrices[d] = prices[s]+p
            
            prices = tempPrices
        
        return -1 if prices[dst]== float("inf") else prices[dst]