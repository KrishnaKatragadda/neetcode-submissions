class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        best = 0

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            best = max(best,area)
            if heights[l] > heights[r]:
                r-=1
            else:
                l +=1
        
        return best 
        