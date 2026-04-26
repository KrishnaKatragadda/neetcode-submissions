class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        l = []
        for i in s:
            if i in par:
                if l and par[i]==l.pop():
                    pass
                else:
                    return False
            else: l.append(i)

        return True if len(l)==0 else False
        