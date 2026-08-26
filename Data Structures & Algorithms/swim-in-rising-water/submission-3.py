# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         ## this graph setup is already provided as a Matrix, so no need to create a adj.
#         ## starting point is [0,0] and there is destination [n-1, n-1]
#         ## I need to find the minimum cost to reach there, so Djikstras algorithm

#         ROWS, COLS = len(grid), len(grid[0])
#         directions = [[0,1],[0,-1],[1,0],[-1,0]]
#         minH = [[grid[0][0],0,0]] ## initialising the minHeap with first position
#        # time = 0
#         currMax = grid[0][0]
#         visit = set()

#         while minH:
#             cost, dst = heapq.heappop(minH)
#             r,c = dst[0],dst[1]
#             if (r,c) in visit:
#                 continue
#             if r == ROWS-1 and c == COLS-1:
#                 return time
#             visit.add((r,c))
#             # if currMax < grid[r][c]:
#             #     currMax = max(currMax, grid[r][c])
#             #     time = time+cost
            

#             ## Now i need to explore the neighbors

#             for d in directions:
#                 if r+d[0] <0 or r+d[0] == ROWS or c+d[1] <0 or c+d[1] == COLS or (r+d[0], c+d[1]) in visit: ## this is boundary conditions
#                     continue
                
#                 newCost = grid[r+d[0]][c+d[1]] - grid[r][c]
#                 currMax = max(currMax, grid[r][c])

#                 heapq.heappush(minH, [newCost,(r+d[0],c+d[1])])
        
#         return time
                


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        # cost, row, col
        minH = [(grid[0][0], 0, 0)]

        visit = set()

        while minH:
            cost, r, c = heapq.heappop(minH)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return cost

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    (nr, nc) in visit
                ):
                    continue

                newCost = max(cost, grid[nr][nc])

                heapq.heappush(minH, (newCost, nr, nc))

