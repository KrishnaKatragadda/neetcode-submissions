class Solution {
    public int largestRectangleArea(int[] heights) {
        
        int n = heights.length;
        Stack<int[]> s = new Stack<>();
        int max = 0;

        for (int i=0; i<n; i++) {

            if (s.isEmpty()) {
                s.push(new int[]{0, heights[i]});
            } else {
                int lastPoppedIndex = -1;
                while (!s.isEmpty() && s.peek()[1] > heights[i]) {
                    max = Math.max(max, (i-s.peek()[0]) * s.peek()[1]);
                    lastPoppedIndex = s.pop()[0];
                }
                lastPoppedIndex = lastPoppedIndex == -1 ? i : lastPoppedIndex;
                s.push(new int[]{lastPoppedIndex, heights[i]});
            }
        }

        while (!s.isEmpty()) {
            max = Math.max(max, (n-s.peek()[0]) * s.peek()[1]);
            s.pop();
        }

        return max;
    }
}
