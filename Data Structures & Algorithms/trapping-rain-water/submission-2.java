class Solution {

    public int trap(int[] height) {
        
        int n = height.length;
        int l=0, r=n-1, lm=0, rm=0, ans=0;

        while (l <= r) {

            if (lm < rm) {
                lm = Math.max(lm, height[l]);
                ans += lm-height[l];
                l++;
            } else {
                rm = Math.max(rm, height[r]);
                ans += rm-height[r];
                r--;
            }
        }

        return ans;
    }

    public int trap1(int[] height) {
        
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
