class Solution {
    public int rob(int[] nums) {
        int dp0=0, dp1=0;

        for (int num : nums) {
            int t = dp1;
            dp1 = Math.max(dp0+num, dp1);
            dp0=t;
        }

        return dp1;
    }
}
