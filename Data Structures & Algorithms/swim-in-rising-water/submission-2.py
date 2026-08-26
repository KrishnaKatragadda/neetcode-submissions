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