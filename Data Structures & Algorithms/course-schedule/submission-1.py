class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## we need to convert the given problem statement into a data structre
        ## we use adjacency list for graph representation
        
        ## step1: if the graph is not grid, you need to construct a adj list
        pre = {i:[] for i in range(numCourses)}
        
        for crs,req in prerequisites:
            pre[crs].append(req)
        
        ## step2: it doesn't hurt to have a visited set again
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if pre[crs]=="[]":
                return True
            
            visited.add(crs)
            for c in pre[crs]:
                if not dfs(c): return False
## lets, say 3 has a prereq of 4. 
## 4 has no prereq so it is [] and returns True
## so you can update 3 as [] ture
            visited.remove(crs)
            pre[crs] ="[]" ## this node has retured
            return True
            
        for i in range(numCourses):
            if not dfs(i): return False ## if the overall traversal gave back False
        
        return True