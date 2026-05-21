class TreeNode:
    def __init__(self): ## at every node, branch, character, it will have a hash set and a flag column
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode() ## initiate root as empty Node
        

    def insert(self, word: str) -> None:
        curr = self.root

        ## 1. move to the root, which is begining
        ## 2. loop through the given word, check if already present
        ## 3. if not, insert it

        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        
        