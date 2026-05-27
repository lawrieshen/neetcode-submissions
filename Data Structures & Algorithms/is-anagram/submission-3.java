class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> counter_s = new HashMap<>();
        Map<Character, Integer> counter_t = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c_s = s.charAt(i);
            char c_t = t.charAt(i);
            counter_s.put(c_s, counter_s.getOrDefault(c_s, 0) + 1);
            counter_t.put(c_t, counter_t.getOrDefault(c_t, 0) + 1);
        }

        return counter_s.equals(counter_t);
    }
}
