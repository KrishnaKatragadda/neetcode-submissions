class Solution {
    public boolean isValid(String s) {
        
        Map<Character, Character> m = new HashMap<>();
        m.put(')', '(');
        m.put('}', '{');
        m.put(']', '[');

        Stack<Character> st = new Stack<>();

        for (char c : s.toCharArray()) {
            if (m.containsKey(c)) {
                if (st.isEmpty() || m.get(c) != st.pop()) return false; 
            } else {
                st.push(c);
            }
        }

        return st.isEmpty();
    }
}
