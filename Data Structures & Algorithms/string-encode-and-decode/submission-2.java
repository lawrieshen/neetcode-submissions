class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String s : strs) {
            encoded.append(s.length()).append('#').append(s);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            int j = str.indexOf('#', i);
            int length = Integer.parseInt(str.substring(i, j));
            j++; // move pass '#'
            decoded.add(str.substring(j, j + length));
            i = j + length;
        }

        return decoded;
    }
}
