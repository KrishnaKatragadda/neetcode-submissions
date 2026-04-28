class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack =[]

        for i,j in enumerate(temperatures):
            while stack and stack[-1][0] < j:
                result[stack[-1][1]]= i-stack[-1][1]
                stack.pop()
            stack.append((j,i))
        
        return result
        