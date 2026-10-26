class Solution {

    public String encode(List<String> strs) {

        StringBuilder res = new StringBuilder();
        for (String s : strs) {
            res.append(s.length()).append('#').append(s);
        }

        return res.toString();
    }

    public List<String> decode(String str) {

        List<String> res = new ArrayList<>();

        int i=0, j=0;

        while (i < str.length()) {
            j=i;
            while (str.charAt(j) != '#') j++;

            Integer l = Integer.parseInt(str.substring(i, j));
            res.add(str.substring(j+1, j+1+l));

            i=j+1+l;
        }

        return res;
    }
}
