class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> cache = new HashSet<>();
        int left = 0;
        int longest = 0;

        for (int right = 0; right < n; right++) {
            Character c = s.charAt(right);

            while (cache.contains(c)) {
                cache.remove(s.charAt(left));
                left++;
            }

            cache.add(c);
            longest = Math.max(longest, right - left + 1);
        }

        return longest;
    }
}
