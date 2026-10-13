class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for i in range(len(t)):
            need[t[i]] = need.get(t[i],0) + 1
        need_count = len(need) 

        window = {}
        have = 0
        l =0
        res = ""
        res_count = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if (r-l+1) < res_count:
                    res = s[l:r+1]
                    res_count = r-l+1
                
                left = s[l]
                window[left] -= 1
                if left in need and window[left] < need[left]:
                    have -= 1
                l+=1
        return res 


            


        
        
        