class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## step1, we have to do graph representation.
        ## convert the given setup into graph
        count = 0
        graph = {i:[] for i in range(n)}

        for v,e in edges:
            graph[v].append(e)
            graph[e].append(v)
            ## this is undirected graph
        visit = set()
        def dfs(node,parent):
            if node in visit: ## we have already explored the node
                return
            
            visit.add(node) ## mark the node as visited

            ## loop through the neighbors
            for nei in graph[node]:
                ## as this in undirected graph, nodes will come in twice
                if nei == parent:
                    continue
                dfs(nei,node)
            
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                count+=1
        
        return count
