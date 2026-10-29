class Solution {
    public int findMin(int[] nums) {
        
        int l=0, r=nums.length-1, m=0;

        while (l<r) {
            m = (l + r)/2;

            if (nums[m] < nums[r]) {
                r = m;
            } else {
                l = m+1;
            }
        }

        return nums[l];
    }
}
