class Solution {
    public int minCostClimbingStairs(int[] cost) {

        int dp0=0, dp1=0, dp2=0;

        for (int i=cost.length-1; i>=0; i--) {
            dp0 = Math.min(dp1, dp2) + cost[i];
            dp2 = dp1;
            dp1 = dp0;
        }

        return Math.min(dp1, dp2);
    }
}
