class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums.length == 0) {
            return new int[0];
        }

        Map<Integer, Integer> cache = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (cache.containsKey(complement)) {
                return new int[]{cache.get(complement), i};
            }

            cache.put(nums[i], i);
        }

        return new int[0];
    }
}
