class Solution {
    public int largestRectangleArea(int[] heights) {
        
        int n = heights.length;
        Stack<int[]> s = new Stack<>();
        int max = 0;

        for (int i=0; i<n; i++) {

            if (s.isEmpty()) {
                s.push(new int[]{0, heights[i]});
            } else {
                int startIndex = i;
                while (!s.isEmpty() && s.peek()[1] > heights[i]) {
                    max = Math.max(max, (i-s.peek()[0]) * s.peek()[1]);
                    startIndex = s.pop()[0];
                }
                s.push(new int[]{startIndex, heights[i]});
            }
        }

        while (!s.isEmpty()) {
            max = Math.max(max, (n-s.peek()[0]) * s.peek()[1]);
            s.pop();
        }

        return max;
    }
}
