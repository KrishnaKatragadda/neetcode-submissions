class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        res=0
        charSet = set() ## maintain this to check if the element is repeated

        ## using sliding window. 
        ## the key is to check, if the current window is valid, 
        ## if not increase or decrease the size.

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res