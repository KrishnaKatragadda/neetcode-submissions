class Solution {
    public int climbStairs(int n) {
        
        double sq5 = Math.sqrt(5);
        double phi1 = (1 + sq5) / 2;
        double phi2 = (1 - sq5) / 2;


        return (int)((Math.pow(phi1, n+1) - Math.pow(phi2, n+1))/sq5);
    }

    public int climbStairs2(int n) {
        
        int dp0=1, dp1=1;
        for (int i=2; i<=n; i++) {
            int t = dp0;
            dp0 = dp0 + dp1;
            dp1 = t;
        }

        return dp0;
    }
}
