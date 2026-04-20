from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set) ## using deafultdict, because if a key is not present
        ## it gets added without a problem
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.': ##if it is empty, no need to check
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or ## check if the value is already present
                    board[r][c] in squares[r//3,c//3]): return False
                
                cols[c].add(board[r][c]) ## if not, add the element to already visited 
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True