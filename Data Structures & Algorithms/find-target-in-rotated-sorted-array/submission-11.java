class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[left] <= nums[mid]) {
                // using left half as the searching scope since it's sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // starting searching in the unsorted part
                if (nums[mid] > target || nums[right] < target) {
                    right = mid - 1; 
                } else {
                    left = mid + 1;
                }
            }
        }

        return -1;
    }
}
