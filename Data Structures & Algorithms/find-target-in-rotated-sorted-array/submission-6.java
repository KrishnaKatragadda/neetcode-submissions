class Solution {

    // Find the mid an try to move away from the sorted part of the array
    public int search(int[] nums, int target) {
        int n = nums.length;
        int l=0, r=n-1;

        while (l <= r) {
            int m = l + (r-l)/2;

            if (nums[m] == target) return m;

            if (nums[m] >= nums[l]) {
                if (target > nums[m] || target < nums[l]) {
                    l = m+1;
                } else {
                    r = m-1;
                }                
            } else {
                if (target < nums[m] ||  target > nums[r]) {
                    r = m-1;
                } else {
                    l = m+1;
                }
            }
        }

        return -1;
    }
}
