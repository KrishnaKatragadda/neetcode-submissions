class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## We can check if a string is palindrome or not in 2 ways
        ## 1st, start at left most and right most and compare and move towards middle, this works for comparing the complete string but not substrings
        ## 2nd, we can start at middle of the string and expand outwards until it is valid.
        ## we will see at every index, if the characters can form a valid palindrome with it at the center.

        res = ""
        resLen = 0
        for i in range(len(s)):

            ## check for odd length strings
            l,r = i,i

            while l>=0 and r<len(s) and s[r] == s[l]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                r+=1
                l-=1
            
            ## checking for even length strings
            
            l,r = i,i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                r+=1
                l-=1
        
        return res
        