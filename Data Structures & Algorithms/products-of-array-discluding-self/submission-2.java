class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int left_mul = 1;
        int right_mul = 1;
        int[] left_product = new int[n];
        int[] right_product = new int[n];

        for (int i = 0; i < n; i++) {
            int j = n - i - 1;
            left_product[i] = left_mul;
            right_product[j] = right_mul;
            left_mul = left_mul * nums[i];
            right_mul = right_mul * nums[j];
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = left_product[i] * right_product[i];
        }
        return result;
    }
}  
