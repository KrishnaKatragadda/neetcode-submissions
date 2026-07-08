class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ## The problem asks for nearest distance,
        ## so we should use BFS, for shortest path, minimum

        visited = set() ## we dont need it but doing it as practise
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def bfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or grid[r][c]==-1:
                return
            
            visited.add((r,c))
            q.append((r,c))
        
        ## instead of traversing all cells, we just loop through the 
        ## destination points

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0: ## this is treasure
                    q.append((r,c))
                    visited.add((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            
            distance+=1
        