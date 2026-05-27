class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length();
        int result = 1;
        int left = 0;
        int[] counter = new int[26];
        int max_freq = 1;

        for (int right = 0; right < n; right++) {
            char charA = 'A';
            int currentChar = (int) s.charAt(right) - (int) charA;

            counter[currentChar]++;
            max_freq = Math.max(max_freq, counter[currentChar]);

            int window_size = right - left + 1;
            if (window_size > max_freq + k) {
                int charToBeRemoved = (int) s.charAt(left) - (int) charA;
                counter[charToBeRemoved]--;
                left++;
            }

            result = right - left + 1;
        }

        return result;
    }
}
