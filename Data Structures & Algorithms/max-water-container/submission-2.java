class Solution {
    public int maxArea(int[] heights) {
        
        int i=0, j=heights.length-1, res=0;

        while (i < j) {
            int a = Math.min(heights[i], heights[j]) * (j-i);
            if (heights[i] > heights[j]) j--;
            else i++;

            res = Math.max(res, a);
        }

        return res;
    }
}
