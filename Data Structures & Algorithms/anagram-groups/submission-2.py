from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        result = []

        for i in range(len(strs)):
            st = strs[i]
            charSet = [0]*26

            for s in st:
                charSet[ord(s)-ord('a')] = 1 + charSet[ord(s)-ord('a')]
            
            dict1[tuple(charSet)].append(st)
        
        for k,v in dict1.items():
            result.append(v)
            
        
        return result
        