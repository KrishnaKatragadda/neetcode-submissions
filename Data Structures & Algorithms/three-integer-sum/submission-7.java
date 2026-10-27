class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i=0; i<n-2; i++) {
            if (nums[i] > 0) break;
            if (i>0 && nums[i] == nums[i-1]) continue;
            int l=i+1, r=n-1;
            while (l < r) {
                int sum = nums[l] + nums[r];
                int t = -1 * nums[i];
                if (sum == t) {
                    List<Integer> trip = new ArrayList<>();
                    trip.add(nums[i]);
                    trip.add(nums[l]);
                    trip.add(nums[r]);

                    res.add(trip);
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l-1]) l++;
                } else if (sum > t) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return res;
    }
}
