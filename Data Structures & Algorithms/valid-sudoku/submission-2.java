class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        int[] r = new int[9];
        int[] c = new int[9];
        int[] b = new int[9];

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                
                if (board[i][j] == '.') continue;

                int val = board[i][j] - '1', bit = 1 << val, bi = (i/3)*3+(j/3);

                if ((r[i] & bit) > 0 || (c[j] & bit) > 0 || (b[bi] & bit) > 0) return false;

                r[i] |= bit;
                c[j] |= bit;
                b[bi] |= bit;
            }
        }

        return true;
    }
}
