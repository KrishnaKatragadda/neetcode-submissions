class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return 0
        elif len(s) == 1:
            return 1
        best = 0
        dup_set = set()
        l = 0
        r = 1
        dup_set.add(s[l])
        
        while r < len(s):

            while s[r]  in dup_set:
                dup_set.remove(s[l])
                l+=1
            dup_set.add(s[r])
            best = max(best, r-l+1)
            r+=1
        
        return best

        

        
        