class Solution {
    public int climbStairs(int n) {
        
        int dp0=1, dp1=1;
        for (int i=2; i<=n; i++) {
            int t = dp0;
            dp0 = dp0 + dp1;
            dp1 = t;
        }

        return dp0;
    }

    public int climbStairs2(int n) {
        
        int dp0=1, dp1=0;
        for (int i=n-1; i>=0; i--) {
            int t = dp0;
            dp0 = dp0 + dp1;
            dp1 = t;
        }

        return dp0;
    }
}
