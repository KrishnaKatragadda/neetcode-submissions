class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dfs(i):

            if i>=n: ## if the current iteration cross the length of the string
            ## we have reached the limit without finding any issue.
                return True
            
            if i in memo: ## if the position is already explored return that 
                return memo[i]
            for w in wordDict:
                l = len(w)
                if s[i:i+l] == w:
                    if dfs(i+l): 
                        memo[i] = True
                        return True
            memo[i]=False
            return False
        
        return dfs(0)
        