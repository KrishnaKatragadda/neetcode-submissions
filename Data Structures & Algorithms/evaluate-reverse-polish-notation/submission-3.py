class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        li = []
        op = ("+","-","*","/")

        for i in tokens:
            if i not in op:
                li.append(int(i))
            else:
                par2 = li.pop()
                par1 = li.pop()
                if i =="+":
                    res = par1+par2
                    li.append(res)
                elif i =="-":
                    res = par1-par2
                    li.append(res)
                elif i =="*":
                    res = par1*par2
                    li.append(res)
                else:
                    res = int(par1/par2)
                    li.append(res)
        return li[0]
        