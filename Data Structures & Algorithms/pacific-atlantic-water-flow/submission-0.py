class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pcf,atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        ### THe idea is that first row, first column will meet pacific ocean
        ### We can start there and see how long will the water flow from Pacific
        ### same approach can be used for atlantic

        def dfs(r,c,visited,prevH):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or heights[r][c]<prevH:
                return
            visited.add((r,c))
            
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
        
        for r in range(ROWS):
            dfs(r,0,pcf,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        for c in range(COLS):
            dfs(0,c,pcf,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pcf and (r,c) in atl:
                    result.append([r,c])
        

        return result