class TimeMap {

    Map<String, List<Pair<String, Integer>>> m;

    public TimeMap() {
        m = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!m.containsKey(key)) m.put(key, new ArrayList<>());

        m.get(key).add(new Pair<>(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (!m.containsKey(key)) return "";

        List<Pair<String, Integer>> list = m.get(key);

        int l=0, r=list.size()-1;
        String ans = "";
        while (l <= r) {

            int m = l + (r-l)/2;

            Pair<String, Integer> p = list.get(m);

            if (p.getValue() > timestamp) {
                r = m-1;
            } else {
                ans = p.getKey();
                l = m+1;
            }
        }

        return ans;
    }
}
