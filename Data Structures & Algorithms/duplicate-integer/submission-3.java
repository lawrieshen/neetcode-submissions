class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            counter.put(nums[i], counter.getOrDefault(nums[i], 0) + 1);

            if (counter.get(nums[i]) >= 2) {
                return true;
            }
        }

        return false;
    }
}
