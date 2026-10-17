class Solution {
    public int rob(int[] nums) {
        int dp0=0, dp1=0, dp2=0;

        for (int num : nums) {
            dp2 = Math.max(num+dp0, dp1);
            dp0 = dp1;
            dp1 = dp2;
        }

        return dp2;
    }
}
