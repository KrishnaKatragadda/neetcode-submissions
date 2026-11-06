class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> d = new LinkedList<>();
        int n = nums.length;
        int[] res = new int[n-k+1];
        for (int i=0; i<n; i++) {

            while (!d.isEmpty() && nums[d.getLast()] < nums[i]) {
                d.removeLast();
            }
            d.addLast(i);

            if (d.getFirst() < i-k+1) {
                d.removeFirst();
            }

            if (i >= k-1) {
                res[i-k+1] = nums[d.getFirst()];
            }
        }

        return res;
    }
}
