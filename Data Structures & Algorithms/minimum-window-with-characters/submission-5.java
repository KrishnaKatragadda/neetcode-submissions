class Solution {
    public String minWindow(String s, String t) {
        
        Map<Character, Integer> needMap = new HashMap<>();
        Map<Character, Integer> haveMap = new HashMap<>();

        for (char c : t.toCharArray()) {
            needMap.put(c, needMap.getOrDefault(c, 0) + 1);
        }

        int start=-1, end=-1, resLen=Integer.MAX_VALUE, haveCount=0, needCount=needMap.size();
        int l = 0;

        for (int r=0; r<s.length(); r++) {

            char c = s.charAt(r);
            haveMap.put(c, haveMap.getOrDefault(c, 0)+1);

            if (needMap.containsKey(c) && haveMap.get(c).intValue() == needMap.get(c).intValue()) haveCount++;

            while (haveCount == needCount) {

                if (r-l+1 < resLen) {
                    resLen = r-l+1;
                    start = l;
                    end = r;
                }

                c = s.charAt(l);
                haveMap.put(c, haveMap.get(c)-1);
                if (needMap.containsKey(c) && haveMap.get(c) < needMap.get(c)) haveCount--;
                l++;
            }
        }

        return start != -1 ? s.substring(start, end+1) : "";
    }
}
