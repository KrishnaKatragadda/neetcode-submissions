class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [["."]* n for i in range(n) ]

        col = set()
        posd = set()
        negd = set()

        def backtrack(r):

            if r == n: ## check for base condition or solution case
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n): ## exploring through the available options

                if c in col or (r+c) in posd or (r-c) in negd:
                    continue ### check if the choice is valid or not

                col.add(c) ## if yes, take the option as choosed
                posd.add(r+c)
                negd.add(r-c)
                board[r][c] ="Q"

                backtrack(r+1) ## explore next possible cases for this option

                col.remove(c) ## disgard the option and move to other options
                posd.remove(r+c)
                negd.remove(r-c)
                board[r][c]="."

        backtrack(0)

        return res
