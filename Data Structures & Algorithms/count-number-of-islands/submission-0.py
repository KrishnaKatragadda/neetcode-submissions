class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() ## to track the vertices of nodes already visited
        ## we can just track nodes with 1's
        ROWS, COLS = len(grid), len(grid[0])
        count =0

        def dfs(r,c):

            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or grid[r][c]=="0":
                return
            ### if the node is out of matric or it is already visited 
            ### or if it has value is 0

            visited.add((r,c))
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visited) and (grid[r][c]=="1"):
                    count+=1
                    dfs(r,c)
        return count