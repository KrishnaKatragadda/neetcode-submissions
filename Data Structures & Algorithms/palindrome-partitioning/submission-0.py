class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] ## to store the final result set
        part = [] ## to store the intermediate result at index

        def dfs(i):

            ## did you explore through the choice space?
            if i >=len(s):
                res.append(part.copy())
                return
            
            ## now go through the remaining choices
            for j in range(i,len(s)):
                if self.isPali(s,i,j): ## if the current choice is good 
                ## for the condition
                    part.append(s[i:j+1]) ## choose the choise
                    dfs(j+1) ## explore the next possibility
                    part.pop() ##unchoose
        dfs(0)
        return res

    def isPali(self, s, i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i,j = i+1, j-1
        
        return True
