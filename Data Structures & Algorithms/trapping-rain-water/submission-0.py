class Solution:
    def trap(self, height: List[int]) -> int:
        ## Given task if to compare two elements and determine an outcome.
        ## we can go ahead and use, two pointer techique
        ## we cannot perform sort here

        water = 0
        lmax = 0
        rmax = 0
        l = 0
        r = len(height)-1

        while l<r:
            if height[l]<height[r]: ## this means lmax is less, move left pointer
                lmax = max(lmax,height[l])
                water+= (lmax - height[l])
                print(water)
                l+=1
            else:
                rmax = max(rmax,height[r])
                water+= (rmax-height[r])
                print(water)
                r-=1

        return water

        