class Solution {
    public String minWindow(String s, String t) {
        int lenS = s.length();
        int lenT = t.length();
        if (lenS == 0 || lenT == 0) return "";

        // Count characters in t
        Map<Character, Integer> tCount = new HashMap<>();
        for (char c : t.toCharArray()) {
            tCount.put(c, tCount.getOrDefault(c, 0) + 1);
        }
        int required = tCount.size();

        // Sliding window
        int left = 0, right = 0, formed = 0;
        Map<Character, Integer> windowCount = new HashMap<>();
        int minLength = Integer.MAX_VALUE;
        int minLeft = 0, minRight = 0;

        while (right < lenS) {
            char c = s.charAt(right);
            windowCount.put(c, windowCount.getOrDefault(c, 0) + 1);

            if (tCount.containsKey(c) && windowCount.get(c).intValue() == tCount.get(c).intValue()) {
                formed++;
            }

            // shrinking form left to right
            while (left <= right && formed == required) {
                // update minimum
                int window_size = right - left + 1;
                if (window_size < minLength) {
                    minLength = window_size;
                    minLeft = left;
                    minRight = right;
                }
                
                char outgoing = s.charAt(left);
                windowCount.put(outgoing, windowCount.get(outgoing) - 1);
                if (tCount.containsKey(outgoing) && windowCount.get(outgoing) < tCount.get(outgoing)) {
                    formed--;
                }
                left++;
            }

            right++;
        }

        return minLength == Integer.MAX_VALUE ? "" : s.substring(minLeft, minRight + 1);
    }
}
