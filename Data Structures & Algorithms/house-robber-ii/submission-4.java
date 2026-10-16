class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n==1) return nums[0];
        return Math.max(nums[0] + help(nums, 2, n-2), help(nums, 1, n-1));
    }

    private int help(int[] nums, int l, int r) {

        int n = r-l+1;
        if (n<=0) return 0;
        if (n==1) return nums[l];
        int dp0 = nums[l], dp1 = Math.max(nums[l], nums[l+1]);
        l = l+2;
        while (l<=r) {
            int t = dp1;
            dp1 = Math.max(nums[l] + dp0, dp1);
            dp0 = t;
            l++;
        }

        return dp1;
    }
}
