class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        best = 0
        dup_set = set()
        l = 0
        
        
        
        for r in range(len(s)):

            while s[r]  in dup_set:
                dup_set.remove(s[l])
                l+=1
            dup_set.add(s[r])
            best = max(best, r-l+1)
            
        
        return best

        

        
        