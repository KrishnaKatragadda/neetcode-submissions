class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dToc = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def dfs(i,currS):

            if len(currS)==len(digits): ## base condition met for us to consider it as result
                res.append(currS)
                return
            
            for c in dToc[digits[i]]: ## available choices, you can make at this stage
                dfs(i+1,currS+c)
        
        if digits:
            dfs(0,"")
        
        return res