class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Map<Character, Integer> m = new HashMap<>();
        int ans = 0, start=0;
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (m.containsKey(c) && m.get(c) >= start) {
                start = m.get(c)+1;
            }
            ans = Math.max(ans, i-start+1);
            m.put(s.charAt(i), i);
        }
        return ans;
    }
}
