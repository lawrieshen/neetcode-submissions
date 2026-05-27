class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            s.add(num);
        }
        
        int longest = 0;

        for (int i = 0; i < nums.length; i++) {
            
            int num = nums[i];
            
            if (!s.contains(num - 1)) {
                // this means this is a starting point of a sequence
                int nextNum = num + 1;
                int length = 1;
                while (s.contains(nextNum)) {
                    nextNum++;
                    length++;
                }

                longest = Math.max(longest, length);
            }
        }

        return longest;
    }
}
