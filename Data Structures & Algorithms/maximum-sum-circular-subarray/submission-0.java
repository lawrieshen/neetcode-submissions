class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int maxSub = nums[0];
        int minSub = nums[0];
        int totalSum = 0;
        
        int curMax = 0;
        int curMin = 0;

        for (int num : nums) {
            totalSum += num;

            // 1. Standard Kadane to find Maximum Subarray
            if (curMax < 0) {
                curMax = 0;
            }
            curMax += num;
            maxSub = Math.max(maxSub, curMax);

            // 2. Modified Kadane to find Minimum Subarray
            if (curMin > 0) {
                curMin = 0;
            }
            curMin += num;
            minSub = Math.min(minSub, curMin);
        }

        // 3. Handle the edge case where all numbers are negative
        if (maxSub < 0) {
            return maxSub;
        }

        // 4. Return the maximum of non-circular and circular subarrays
        return Math.max(maxSub, totalSum - minSub);
    }
}
