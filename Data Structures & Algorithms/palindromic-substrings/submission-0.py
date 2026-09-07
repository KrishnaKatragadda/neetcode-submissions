class Solution:
    def countSubstrings(self, s: str) -> int:
        ## For every palindrome problem, you need to consider 
        ## odd length string and even length string cases and handle them

        res = 0 ## tracks the number of palindrome substring

        for i in range(len(s)):
            ## Odd length
            left, right = i,i

            while left >=0 and right<len(s) and s[left]==s[right]:
                res+=1 ## adding the number of palindromes seen

                left-=1
                right+=1
            
            ## even length

            left, right = i, i+1

            while left>=0 and right<len(s) and s[left]==s[right]:
                res+=1

                left-=1
                right+=1
        
        return res
        