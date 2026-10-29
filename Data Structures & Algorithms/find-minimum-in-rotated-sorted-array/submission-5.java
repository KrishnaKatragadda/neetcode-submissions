class Solution {
    public int findMin(int[] nums) {
        
        int l=0, r=nums.length-1, m=0;

        if (nums[r] >= nums[l]) return nums[l];

        while (l<=r) {
            m = (l + r)/2;

            if (m > 0 && nums[m-1] > nums[m]) return nums[m];

            if (nums[m] >= nums[l] && nums[r] < nums[m]) {
                l = m+1;
            } else {
                r = m-1;
            }
        }

        return nums[m];
    }
}
