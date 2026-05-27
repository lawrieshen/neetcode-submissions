class Solution {
    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int numIslands(char[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        int islands = 0;

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    islands++;
                }
            }
        }

        return islands;
    }

    private void dfs(char[][] grid, int i, int j) {
        if (i >= 0 && i <  grid.length && j >= 0 && j < grid[0].length && grid[i][j] == '1') {
            grid[i][j] = '0';

            for (int[] d: directions) {
                dfs(grid, i + d[0], j + d[1]);
            }
        }
    }
}
