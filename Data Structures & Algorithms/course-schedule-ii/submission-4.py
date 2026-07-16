class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ### step1: we need to represent graph in a adjacency list 
        res =[]
        pre = {i:[] for i in range(numCourses)}

        for crs, req in prerequisites:
            pre[crs].append(req)
        ## now, we have adjacency list representation of graph
        visited = set() ## to keep track of what is already processed
        visiting = set() ## what is being processed in present recursion stack or call
        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting: ## checking for cycle, so checking in the same execution call
                return False
            
            # if pre[crs]==[]:
            #     return True
            
            visiting.add(crs)
            ## currently processing the node and looking for any prereqs for it
            for c in pre[crs]:
                if not dfs(c): return False
            
            res.append(crs)
            visiting.remove(crs)
            visited.add(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i): return []


        return res 