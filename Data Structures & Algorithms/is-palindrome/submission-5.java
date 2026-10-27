class Solution {
    public boolean isPalindrome(String s) {
        
        int i=0, j=s.length()-1;
        while (i < j) {
            if (!isAlphaNumeric(s.charAt(i))) i++;
            else if (!isAlphaNumeric(s.charAt(j))) j--;
            else if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            else {
                i++;
                j--;
            }
            
        }

        return true;
    }

    private boolean isAlphaNumeric(char c) {
        return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }
}
