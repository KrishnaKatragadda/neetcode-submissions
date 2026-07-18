class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## for a tree to be valid, it should have no cycles in it.

        ## check for cycles in the given graph
        ## no of edges should'nt be should not be greater than n-1
        ## there can be not connected nodes in the graph

        if len(edges)>(n-1):
            return False
        
        ## constructing a adjacency list
        graph = {i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei,node):
                    return False
            
            return True
        ## we need to check, if the number of visited nodes in the pass is equal to n.
        ## if not we have disconnected nodes in the graph
        return dfs(0,-1) and len(visit)==n
        