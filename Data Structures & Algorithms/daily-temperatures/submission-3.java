class Solution {

    public int[] dailyTemperatures1(int[] temp) {
        int n = temp.length;
        int[] res = new int[n];
        for (int i=n-2; i>=0; i--) {
            int j = i+1;

            while (j<n && temp[j] <= temp[i]) {
                if (res[j] == 0) {
                    j=n;
                    break;
                }

                j = j + res[j];
            }

            if (j < n) {
                res[i] = j-i;
            }
        }

        return res;
    }

    public int[] dailyTemperatures(int[] temp) {
        int n = temp.length;
        int[] res = new int[n];
        Stack<Integer> s = new Stack<>();

        for (int i=0; i<n; i++) {
            while (!s.isEmpty() && temp[s.peek()] < temp[i]) {
                res[s.peek()] = i - s.pop();
            }
            s.push(i);
        }

        return res;
    }
}
