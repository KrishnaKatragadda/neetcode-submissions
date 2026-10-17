class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i>=len(s) and j >= len(p):
                return True
            if j>=len(p):
                return False
            
            ### first and foremost
            ### just check if the current char matches or the pattern has '.'
            firstMatch = i <len(s) and (s[i]==p[j] or p[j]=='.')

            ## this will not do, what if the very next character has '*'

            if (j+1)<len(p) and p[j+1]=='*': ## now you have two choices
                cache[(i,j)] = dfs(i,j+2) or (firstMatch and dfs(i+1, j))
                return cache[(i,j)]
            
            ## there is no * in j+1 position
            if firstMatch:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            
            cache[(i,j)] = False
            return cache[(i,j)]
        
        return dfs(0,0)
    