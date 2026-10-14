class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        r = set()
        c = set() 

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)

        for i in r:
            for j in range(COLS):
                matrix[i][j]=0
        
        for i in range(ROWS):
            for j in c:
                matrix[i][j]=0
    
        