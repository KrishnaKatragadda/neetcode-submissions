class Solution {
    public int minCostClimbingStairs(int[] cost) {

        int n = cost.length;
        int n2=0, n1=cost[n-1];
        for (int i=n-2; i>=0; i--) {
            int t = n1;
            n1 = Math.min(n2, n1)+cost[i];
            n2 = t;
        }

        return Math.min(n1, n2);
    }
}
