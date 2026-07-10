class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        fresh = 0
        visited =set()
        ROWS, COLS = len(grid),len(grid[0])
        q = deque()

        def bfs(r,c): ## we will apply bfs to start from multiple starting points
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or grid[r][c]!=1:
                return False
            
            visited.add((r,c))
            grid[r][c]=2
            q.append((r,c))
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visited) and (grid[r][c]==2):
                    visited.add((r,c))
                    q.append((r,c)) ### All the initial rotten fruits are added to queue
                elif grid[r][c]==1:
                    fresh+=1
        
        if fresh ==0: return 0
        
        ## actual bfs traversal
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                print(r,c)
                if bfs(r+1,c): fresh-=1
                if bfs(r-1,c): fresh-=1
                if bfs(r,c+1): fresh-=1
                if bfs(r,c-1): fresh-=1
            count+=1
            
            print(count)
        
        return count if fresh ==0 else -1
        # flag = False
        # for r in range(ROWS):
        #     if 1 in grid[r]:
        #         flag = True
        
        # return -1 if flag else count