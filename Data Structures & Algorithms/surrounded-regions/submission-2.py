class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ## the idea is that,if the region reaches to border by any chance
        ## so we will look through the borders, if we find any
        ## cell that is 0, we apply dfs. if it reaches and forms a region
        ## all those cells are needed to be unchanges
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O":
                return
            
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        ##step1: loop through the boarder and call dfs

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c]=="O") and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    capture(r,c)
        
        ## step2: marks all the cells as X, where it is O now
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        ## step3: revert back all the T as O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="T":
                    print("YES")
                    board[r][c]="O"
        