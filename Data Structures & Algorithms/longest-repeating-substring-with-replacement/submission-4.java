class Solution {
    public int characterReplacement(String s, int k) {
        
        int ans=0, maxf=0, l=0;

        Map<Character, Integer> m = new HashMap<>();

        for (int r=0; r<s.length(); r++) {

            char c = s.charAt(r);
            m.put(c, m.getOrDefault(c, 0)+1);
            maxf = Math.max(maxf, m.get(c));

            while (l<=r && r-l+1-maxf > k) {
                m.put(s.charAt(l), m.get(s.charAt(l))-1);
                l++;
            }

            ans = Math.max(r-l+1, ans);
        }

        return ans;
    }
}
