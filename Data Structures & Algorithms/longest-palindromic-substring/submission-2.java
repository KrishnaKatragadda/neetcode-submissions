class Solution {

    int st=0, e=0;
    public String longestPalindrome(String s) {
        
        int n = s.length();
        for (int i=0; i<n; i++) {
            check(s, i, i);
            check(s, i, i+1);
        }

        return s.substring(st, e+1);
    }

    private void check(String s, int x, int y) {
        int len=0,i=x,j=y;
        while (i >=0 && j<s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        i++;
        j--;
        len = j-i+1;
        if (len > e-st+1) {
            st=i++;
            e=j--;
        }
    }
}
