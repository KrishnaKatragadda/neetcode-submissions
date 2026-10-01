class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ## this is a 2D dynamic programming problem
        ## if we are able to each the end of s3 with help of s1 and s2, it is TRUE

        ## check if the len of strings add up to s3

        if len(s1)+len(s2) !=len(s3): return False

        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]

        dp[len(s1)][len(s2)] = True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):

                if i <len(s1) and s1[i]==s3[i+j] and dp[i+1][j]==True:
                    dp[i][j]=True
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]==True:
                    dp[i][j]=True
        return dp[0][0]

        