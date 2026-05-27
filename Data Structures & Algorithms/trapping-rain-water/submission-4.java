class Solution {
    public int trap(int[] height) {
        int n = height.length;

        int left_wall = 0;
        int right_wall = 0;

        int[] max_left = new int[n];
        int[] max_right = new int[n];

        for (int i = 0; i < n; i++) {
            int j = (n - 1) - i;
            
            max_left[i] = left_wall;
            max_right[j] = right_wall;

            left_wall = Math.max(left_wall, height[i]);
            right_wall = Math.max(right_wall, height[j]);
        }

        int water = 0;

        for (int i = 0; i < n; i++) {
            int pot = Math.min(max_left[i], max_right[i]) - height[i];
            water += Math.max(0, pot);
        }

        return water;
    }
}
