class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int left = 0;
        int right = n - 1;
        int max_area = 0;

        while (left < right){
            int area = Math.min(heights[left], heights[right]) * Math.abs(left - right);
            max_area = Math.max(max_area, area);

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return max_area;
    }
}
