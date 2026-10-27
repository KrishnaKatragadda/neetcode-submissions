class Solution {
    public int trap(int[] height) {
        
        int n = height.length;
        int[] lm = new int[n];

        lm[0] = height[0];
        for (int i=1; i<n; i++) {
            lm[i] = Math.max(lm[i-1], height[i]);
        }

        int rm=0,ans=0;
        for (int i=n-1; i>=0; i--) {
            rm = Math.max(rm, height[i]);
            ans += Math.min(lm[i], rm) - height[i];
        }

        return ans;
    }
}
