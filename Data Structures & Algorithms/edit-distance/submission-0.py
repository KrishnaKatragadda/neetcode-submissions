class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        ## this is a 2D dynamic programming problem.

        dp = [[float("inf")]*(len(word1)+1) for _ in range(len(word2)+1)]

        ## define the base case, If the w2 is empty
        ## number of modifications that need to be done on w1 is len(w2) removals

        for i in range(len(word1)+1):
            dp[len(word2)][i] = len(word1)-i
         ## number of modifications that need to be done on w1 is len(w2) additions
        for j in range(len(word2)+1):
            dp[j][len(word1)] = len(word2)-j
        
        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                
                if word2[i]==word1[j]:
                    dp[i][j] = dp[i+1][j+1]
                
                else:
                    dp[i][j] = 1+min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        
        return dp[0][0]
        