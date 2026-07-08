class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set() ## maintain this to track visited nodes
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):

            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or grid[r][c]==0:
                return 0 ## base condition, the return should be consitent return
            
            visited.add((r,c))

            
            return (1+ dfs(r,c+1)+
            dfs(r,c-1)+
            dfs(r+1,c)+
            dfs(r-1,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visited) and grid[r][c]==1:
                    maxArea = max(maxArea,dfs(r,c))
        
        return maxArea
                
        