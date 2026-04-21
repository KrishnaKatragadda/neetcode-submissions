class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum()).lower()
        print(cleaned)
        if len(cleaned)==0: return True

        left = 0
        right = len(cleaned)-1

        while left<right:
            if cleaned[left]==cleaned[right]:
                left+=1
                right-=1
            else:
                return False
        
        return True
        