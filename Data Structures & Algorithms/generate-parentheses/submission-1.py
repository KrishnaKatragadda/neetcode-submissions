class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[] ## to store the current path
        res = []
##### You have a choice space, choose from available which satisfies the give
##### conditions
        def helper(openN, closeN):

            if openN == closeN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(") ## choose
                helper(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")") ## choose
                helper(openN, closeN+1)
                stack.pop()

        helper(0,0)

        return res