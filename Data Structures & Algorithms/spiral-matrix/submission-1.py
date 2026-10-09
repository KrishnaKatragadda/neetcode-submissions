class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # ROWS,COLS = len(matrix),len(matrix[0])
        # visited = set()
        # res =[]
##YOU FCKER, DFS DOESNT work here
        # def dfs(r,c):

        #     if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited:
        #         return
            
        #     visited.add((r,c))
        #     res.append(matrix[r][c])
        #     dfs(r,c+1)
        #     dfs(r+1,c)
        #     dfs(r,c-1)
        #     dfs(r-1,c)
        

        

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r,c) not in visited:
        #             dfs(r,c)
        
        # print(res)
        # return res

### have pointers at top and bottom row. have pointers at last column and first column. iterative through them
        res =[]
        ROWS, COLS = len(matrix), len(matrix[0])
## ROW iterators
        left = 0 
        right = ROWS-1
## COL iterators
        c1 = COLS-1
        c2 = 0
        while left <= right and c2 <= c1:

            # Top row
            for c in range(c2, c1 + 1):
                res.append(matrix[left][c])
            left += 1

            # Right column
            for r in range(left, right + 1):
                res.append(matrix[r][c1])
            c1 -= 1

            # Bottom row
            if left <= right:
                for c in range(c1, c2 - 1, -1):
                    res.append(matrix[right][c])
                right -= 1

            # Left column
            if c2 <= c1:
                for r in range(right, left - 1, -1):
                    res.append(matrix[r][c2])
                c2 += 1

        return res
