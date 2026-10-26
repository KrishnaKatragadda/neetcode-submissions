class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> m = new HashMap<>();
        List<Integer>[] f = new ArrayList[nums.length+1];

        for (int num : nums) m.put(num, m.getOrDefault(num, 0)+1);

        for (Map.Entry<Integer, Integer> e : m.entrySet()) {
            int key = e.getKey(), val = e.getValue();
            
            if (f[val] == null) f[val] = new ArrayList<>();
            f[val].add(key);
        }

        int[] res = new int[k];
        int i=0;

        for (int j=nums.length; j>=0; j--) {
            if (f[j] != null) {
                for (int num : f[j]) {
                    res[i++] = num;
                    if (i == k) return res;
                }
            }
        }

        return res;
    }
}
