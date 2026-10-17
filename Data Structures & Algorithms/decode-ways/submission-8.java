class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int dp0=0, dp1=1, dp2=0;

        for (int i=n-1; i>=0; i--) {

            if (s.charAt(i) == '0') {
                dp0=0;
                dp2 = dp1;
                dp1 = dp0;
            } else {
                dp0 = dp1;
                if (i+1 < s.length() && (s.charAt(i) == '1' || (s.charAt(i) == '2' && s.charAt(i+1) <= '6'))) {
                    dp0+=dp2;
                }
                dp2 = dp1;
                dp1 = dp0;
            } 
        }

        return dp0;
    }
}
