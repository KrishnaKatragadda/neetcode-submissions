class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dfs(i):

            if i>=n:
                return True
            
            if i in memo:
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
        