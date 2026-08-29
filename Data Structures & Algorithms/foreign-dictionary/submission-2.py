class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ## This is a graph problem, so we need to represent the 
        ## situation as a adjacency list.

        adj = {c:set() for w in words for c in w} ## Using a set because e<w comes two times i dont want to add e-- w,w twice right?

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))

            ## lets say abc and ab or er and erf we should just consider len 2
            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            ## abc and ab, so c and '' so invalid
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = set()
        visiting = set()
        res = []

        def dfs(c):
            if c in visiting: ## this is present in current path, so a cycle
                return True
            if c in visited: ## this is already processed completly, no need to process or nothing broke here
                return False
            visiting.add(c) ## if fresh, add it to the current path
            for nei in adj[c]: ## explore the neighbors, here the outgoing childs
                if dfs(nei): ## 
                    return True
            visited.add(c) ## now the c is completly processed
            visiting.remove(c) ## remove it from path
            res.append(c) ## add it to result 

            ## this is post order DFS reverse (topological sort)
            ##left, right, node

            return False
    
        for c in adj:
            if dfs(c):
                return ""
        res.reverse() ## reverse
        return "".join(res)
        

        