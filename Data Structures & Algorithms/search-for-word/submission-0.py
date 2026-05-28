class TriNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def insert(self,word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w]=TriNode()
            curr = curr.children[w]
        curr.isWord = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r,c,root):
            curr = root
            if r<0 or c<0 or r==ROWS or c == COLS or (r,c) in visited or board[r][c] not in curr.children:
                return
            curr = curr.children[board[r][c]]
            if curr.isWord:
                Flag[0] = True
            
            visited.add((r,c))
            dfs(r+1,c, curr)
            dfs(r-1,c, curr)
            dfs(r,c+1, curr)
            dfs(r,c-1, curr)
            visited.remove((r,c))
        
        Flag = [False]
        visited = set()

        root = TriNode()
        root.insert(word)
        # for w in word:
        #     print(root.children)
        #     root = root.children[w]
        # print(root.isWord)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        

        return Flag[0]
        


        