class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> cache = new HashMap<>(); // residual -> index

        for (int i = 0; i < nums.length; i++) {
            int residual = target - nums[i];

            if (!cache.containsKey(residual)) {
                cache.put(nums[i], i);
            } else {
                return new int[]{cache.get(residual), i};
            }
        }

        throw new IllegalArgumentException("No two sum solution found");
    }
}
