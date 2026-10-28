class Solution {
    public int[] dailyTemperatures(int[] temp) {
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
}
