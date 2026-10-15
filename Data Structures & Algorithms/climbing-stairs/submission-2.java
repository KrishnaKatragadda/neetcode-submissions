class Solution {
    public int climbStairs(int n) {
        if (n <= 2)
            return n;

        int n1 = 1, n2 = 2, t;

        for (int i=3; i<=n; i++) {
            t = n2;
            n2 = n1 + n2;
            n1 = t;
        }

        return n2;
    }
}
