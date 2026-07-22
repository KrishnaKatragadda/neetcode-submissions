class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ## step1: construct an adjacency list from the graph info

        # graph = {i:[] for i in range(1,len(edges)+1)}
        
        # for v,e in edges:
        #     graph[v].append(e)
        #     graph[e].append(v)
        
        ## step2: there will be a cycle for sure, we need to identify 
        ## all the connections in the graph
        ## I know how to detect a cycle, but how to identify the actual cycle.

        ## that's exactly what UNION-FIND helps us to answer -- introducing what node contribute to a cycle.
        ## Union-Find helpe keep track of what nodes are connected

        ## create independent sets representing nodes and parents

        n = len(edges)
        parent =[i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(u): ## this gives the root of the current node, like root
            if parent[u]!=u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(x,y): ## can i union them with out a problem
        ## Yes, you can but i have a problem if you cause a cycle
            parent_x = find(x)
            parent_y = find(y)

            if parent_x == parent_y:
                return False ## both nodes have same parent, so if we connect them
                ## it will be a cycle
            
            if rank[parent_x] > rank[parent_y]: ## assiging nodes to the roots
                parent[parent_y] = parent[parent_x]
            elif rank[parent_y] > rank[parent_x]:
                parent[parent_x] = parent[parent_y]
            else:
                parent[parent_x] = parent_y
                rank[parent_y]+=1 ## updating the rank

            return True 
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]

        