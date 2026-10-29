class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int max = 0, n = piles.length;

        for (int i=0; i<n; i++) {
            max = Math.max(max, piles[i]);
        }

        int l=1, r=max, ans=max;

        while (l <= r) {

            int m = l + (r-l)/2;

            int t = 0;

            for (int i=0; i<n; i++) {
                t += Math.ceil((double)piles[i]/m);
            }

            if (t <= h) {
                ans = m;
                r = m-1;
            } else {
                l = m+1;
            }
        }

        return ans;
    }
}
