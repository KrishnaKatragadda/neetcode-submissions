class Solution {
    public boolean canPartition(int[] nums) {

        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 == 1) return false;
        int t = sum/2;
        Set<Integer> sums = new HashSet<>();
        sums.add(0);

        for (int i=nums.length-1; i>=0; i--) {

            Set<Integer> newSums = new HashSet<>();
            for (int s : sums) {
                newSums.add(s + nums[i]);
                newSums.add(s);
            }

            sums = newSums;
        }

        return sums.contains(t);
    }
}
