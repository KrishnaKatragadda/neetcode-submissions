class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 ## this will hold the answer, it is seen as 0000000000000...0000

        for _ in range(32):
            
            bit = n & 1 ## now this bit will store the last bit, it will capture 1 or 0

            res = (res<<1)|bit ## you have created a spot by shifting and insert the bit at left most

            n = n >>1
        
        return res

        