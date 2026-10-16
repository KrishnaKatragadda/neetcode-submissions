class Solution {

    int res=0;
    public int countSubstrings(String s) {
        
        for (int i=0; i<s.length(); i++) {
            check(s, i, i);
            check(s, i, i+1);
        }

        return res;
    }

    private void check(String s, int l, int r) {

        while (l >= 0 && r<s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
            res++;
        }
    }
}
