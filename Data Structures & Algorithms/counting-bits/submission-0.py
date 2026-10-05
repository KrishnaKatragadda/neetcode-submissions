class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []## stores the results here
        for i in range(n+1):
            bits = 0
            while i!=0:
                bits+= (i&1)
                i = i>>1
            
            res.append(bits)
            
        return res 
        