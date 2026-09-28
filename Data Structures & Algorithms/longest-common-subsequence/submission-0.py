class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## this is a 2-Dimensional DP problem.

        ## I need to compare both the strings and figure out what matches

        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):

                ### now if the characters in both strings match, we need to trim both strings by one and move ahead
                if text1[i]==text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1] ## we move diagonal
                else:
                    ## if the characters in both strings doesn't match at that position
                    ## we are not sure which string to trim. so we check both and get the max of either
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]