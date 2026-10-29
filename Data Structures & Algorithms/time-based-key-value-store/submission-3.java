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
        if (list.size() == 0 || list.get(0).getValue() > timestamp) return "";

        int l=0, r=list.size()-1;

        while (l < r) {

            int m = l + (r-l)/2;

            Pair<String, Integer> p = list.get(m);

            if (p.getValue() > timestamp) {
                r = m;
            } else {
                l = m+1;
            }
        }

        String ans;

        if (list.get(l).getValue() <= timestamp) return list.get(l).getKey();

        if (l > 0) return list.get(l-1).getKey();

        return list.get(0).getKey();
    }
}
