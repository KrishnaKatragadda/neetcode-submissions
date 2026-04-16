class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s)!=len(t): return False ## checking if the length is different
        # ## if so, then it breaks it.

        # char1 = set()
        # char2 = set()

        # for i in s:
        #     char1.add(i)
        # for j in t:
        #     char2.add(j)
        
        # if char1 == char2: return True

        # return False

        ## This fails, in cases where the length of strings is same, with 
        ## different frequencies

        # if len(s)!= len(t): return False
        # sum1 = 0
        # sum2 = 0
        # for i in s:
        #     sum1 += ord(i)-ord('a')
        # for j in t:
        #     sum2 += ord(j)-ord('a')
        
        # return True if sum1==sum2 else False
        dict1 = {}
        dict2 = {} ## Always use dict to store freq of elements
        if len(s) != len(t): return False

        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i],0) + 1 ## find the freq of characters in string
            dict2[t[i]] = dict2.get(t[i],0) + 1
        
        return True if dict1 == dict2 else False ## check if the both are identical
