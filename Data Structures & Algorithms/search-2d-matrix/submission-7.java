class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int rows = matrix.length, cols = matrix[0].length;

        int l=0, r=rows*cols-1;

        while (l<r) {
            int m = l + (r-l)/2;

            int i = m/cols, j = m%cols;

            if (matrix[i][j] >= target) {
                r = m;
            } else {
                l = m+1;
            }
        }

        int i = l/cols, j = l%cols;
        return matrix[i][j] == target;
    }
}
