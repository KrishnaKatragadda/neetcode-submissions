class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();

        for (int i=0; i<n-2; i++) {
            if (nums[i] > 0) continue;
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
                    while(l>0 && l<n && nums[l] == nums[l-1]) l++;
                    r--;
                } else if (sum > t) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        

        return new ArrayList<>(res);
    }
}
