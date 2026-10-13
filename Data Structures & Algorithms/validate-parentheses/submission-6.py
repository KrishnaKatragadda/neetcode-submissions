class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(' , ']' : '[', '}' : '{'}
        stack = []
        for i in range(len(s)):
            
            if  s[i] in pairs:
                if not stack or stack.pop() != pairs[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return not stack
        

        