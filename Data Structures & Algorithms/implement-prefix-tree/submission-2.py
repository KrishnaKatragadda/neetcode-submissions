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
        ## 1. move to the root node
        ## 2. loop through the given word
        ## 3. if not present, return False immediatly
        ## 4. if present, move to the next node
        ## 5. after the word is completed, if the word is True or not
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        ## 1. Move to the root node
        ## 2. loop through the given prefix
        ## 3. we just need to check if the prefix follows a path, without breaking
        ## 4. if the path for prefix is not present, return False immediatly
        ## 5. if the prefix is completed along the path, return True
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        
        