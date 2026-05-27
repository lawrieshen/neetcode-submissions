class Solution {
    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

    public int maxAreaOfIsland(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;

        int maxArea = 0;

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j);
                    maxArea = Math.max(maxArea, area);
                }
            }
        }

        return maxArea;
    }

    private int dfs(int[][] grid, int i, int j) {
        int area = 0;
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return area;
        }

        if (grid[i][j] == 1) {
            area++;
            grid[i][j] = 0;
            for (int[] d: directions) {
                area += dfs(grid, i + d[0], j + d[1]);
            }
        }

        return area;
    }
}
