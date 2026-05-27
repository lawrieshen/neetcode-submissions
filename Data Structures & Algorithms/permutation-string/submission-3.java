class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int s1_length = s1.length();
        int s2_length = s2.length();

        if (s1_length > s2_length) {
            return false;
        }
        
        // prepare counters

        Map<Character, Integer> s1_counter = new HashMap<>();
        for (char c : s1.toCharArray()) {
            s1_counter.put(c, s1_counter.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> window_counter = new HashMap<>();
        for (int i = 0; i < s1_length; i++) {
            char c = s2.charAt(i);
            window_counter.put(c, window_counter.getOrDefault(c, 0) + 1);
        }

        if (s1_counter.equals(window_counter)) {
            return true;
        }

        // sliding window
        for (int i = s1_length; i < s2_length; i++) {
            char starting_char = s2.charAt(i - s1_length);
            char new_char = s2.charAt(i);

            // remove the starting char from the counter
            window_counter.put(starting_char, window_counter.getOrDefault(starting_char, 0) - 1);
            if (window_counter.get(starting_char) == 0) {
                window_counter.remove(starting_char);
            }

            // add ne char to window
            window_counter.put(new_char, window_counter.getOrDefault(new_char, 0) + 1);

            // check
            if (s1_counter.equals(window_counter)) {
                return true;
            }
        }

        return false;
    }
}
