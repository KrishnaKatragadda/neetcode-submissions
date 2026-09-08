class Solution:
    def numDecodings(self, s: str) -> int:
        # memo = {} Top - down recursive, Memoization
        # def dfs(i):

        #     ## if the current index is past string length
        #     ## you have found a valid decoding

        #     if i == len(s):
        #         return 1
            
        #     if s[i]=="0":
        #         return 0
        #     if i in memo:
        #         return memo[i]
            
        #     res = dfs(i+1)

        #     if i+1 < len(s) and 10<= int(s[i:i+2]) <27:
        #         res+=dfs(i+2)
            
        #     memo[i]= res
            
        #     return res
        
        # return dfs(0)

        n = len(s)

        dp = [0]*(n+1)

        dp[n] = 1 ## this indicates the end of the string

        for i in range(n-1,-1,-1):

            ## check if the present character is 0, Then we cannot decodeit
            if s[i]=="0":
                dp[i]=0
                continue
            ## if it is not 0, any single charater can be formed
            ## option1: take one digit
            dp[i] = dp[i+1]

            ## option2 Taking 2 characters, we need to make sure it is in range
            if i+1<n and 10<= int(s[i:i+2])<27:
                dp[i]+=dp[i+2] ## we can take one chracter and two as well
            
        return dp[0]
            

        