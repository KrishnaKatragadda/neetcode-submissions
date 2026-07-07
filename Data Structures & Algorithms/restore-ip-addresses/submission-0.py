class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        ## if the given string is greater than length12, it is not valid

        if len(s)>12:
            return res

        def backtrack(i,dots, curIp):
            if dots ==4 and i ==len(s): ## this is valid IP address case, we 
            ## have 4 dots, the index has reached the end of the given string.
                res.append(curIp[:-1])
                return
            
            if dots>4:
                return ## invalid case
            
            for j in range(i, min(i+3,len(s))): ## we start from current index and 
            ## check for next 3 characters, we take min because if the current index is
            ## at last 3 positions, then i+3 will be Out of bound

                if int(s[i:j+1]) < 256 and (i==j or s[i]!="0"):
                    ## checking if the current combination is less than 256
                    ## and the current word doesnt start with leading 0
                    backtrack(j+1, dots+1, curIp+s[i:j+1]+".")
        backtrack(0,0,"")
        return res