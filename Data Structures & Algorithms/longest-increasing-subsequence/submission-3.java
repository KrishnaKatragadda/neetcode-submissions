class Solution {
    public int lengthOfLIS(int[] nums) {
        
        List<Integer> lis = new ArrayList<>();
        lis.add(nums[0]);
        int res = 1;
        for (int i=1; i<nums.length; i++) {
            if (lis.get(lis.size()-1) < nums[i]) {
                lis.add(nums[i]);
                res++;
            } else {
                lis.set(binSearch(lis, nums[i]), nums[i]);
            }
        }

        return res;
    }

    private int binSearch(List<Integer> lis, int v) {
        int l=0, r=lis.size()-1;

        while (l<r) {
            int m = l+(r-l)/2;
            if (lis.get(m) >= v) {
                r = m;
            } else {
                l = m + 1;
            }
        }

        return l;
    }
}