class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        
        int n = speed.length;
        int[][] pair = new int[n][2];

        for (int i=0; i<n; i++) {
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }

        Arrays.sort(pair, (a,b) -> Integer.compare(a[0], b[0]));

        Stack<int[]> s = new Stack<>();
        for (int i=n-1; i>=0; i--) {

            if (s.isEmpty()) {
                s.push(pair[i]);
            } else {
                double time1 = (double)(target - pair[i][0]) / pair[i][1];
                double time2 = (double)(target - s.peek()[0]) / s.peek()[1];

                if (time2 < time1) s.push(pair[i]);
            }
        }

        return s.size();
    }
}
