class Solution {
    public int rob(int[] nums) {
        
        int n = nums.length;

        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);

        int n1=nums[0], n2=Math.max(nums[1],nums[0]), t;
        for (int i=2; i<n; i++) {
            t = n2;
            n2 = Math.max(n1+nums[i], n2);
            n1 = t;
        }

        return n2;
    }
}
