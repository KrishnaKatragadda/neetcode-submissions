class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> ans = new HashMap<>();
        for (String s : strs) {

            int[] f = new int[26];
            for (Character c : s.toCharArray()) {
                f[c-'a']++;
            }

            String k = Arrays.toString(f);
            
            if (!ans.containsKey(k)) ans.put(k, new ArrayList<>());
            ans.get(k).add(s);
        }

        return new ArrayList<>(ans.values());
    }
}
