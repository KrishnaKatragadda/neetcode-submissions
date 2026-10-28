class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int s=0, e=matrix.length;
        while (s < e) {
            int m = s + (e-s)/2;

            if (matrix[m][0] >= target) {
                e = m;
            } else {
                s = m+1;
            }
        }
        
        if (s < matrix.length && matrix[s][0] == target) return true;

        int row = s-1;

        if (row < 0) return false;
        s=0;
        e = matrix[0].length;

        while (s < e) {
            int m = s + (e-s)/2;

            if (m > -1 && m < matrix[0].length && matrix[row][m] >= target) {
                e = m;
            } else {
                s = m+1;
            }
        }

        return s < matrix[0].length && matrix[row][s] == target;
    }
}
