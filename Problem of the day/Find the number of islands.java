//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int m = Integer.parseInt(s[1]);
            char[][] grid = new char[n][m];
            for (int i = 0; i < n; i++) {
                String[] S = br.readLine().trim().split(" ");
                for (int j = 0; j < m; j++) {
                    grid[i][j] = S[j].charAt(0);
                }
            }
            Solution obj = new Solution();
            int ans = obj.numIslands(grid);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends

class Solution {
    // Function to find the number of islands.
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        int n = grid.length;
        int m = grid[0].length;
        int islandCount = 0;

        // Directions for the 8 possible movements (up, down, left, right, and diagonals)
        int[] rowDir = {-1, 1, 0, 0, -1, -1, 1, 1};
        int[] colDir = {0, 0, -1, 1, -1, 1, -1, 1};

        // Iterate over every cell in the grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // If we find land ('1'), start a DFS (iteratively)
                if (grid[i][j] == '1') {
                    islandCount++;
                    // Perform DFS using a stack
                    Stack<int[]> stack = new Stack<>();
                    stack.push(new int[]{i, j});
                    grid[i][j] = '0';  // Mark it as visited

                    // Process all connected lands using DFS
                    while (!stack.isEmpty()) {
                        int[] current = stack.pop();
                        int row = current[0];
                        int col = current[1];

                        // Explore all 8 possible directions
                        for (int k = 0; k < 8; k++) {
                            int newRow = row + rowDir[k];
                            int newCol = col + colDir[k];

                            // Check if the new position is within bounds and is land
                            if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && grid[newRow][newCol] == '1') {
                                stack.push(new int[]{newRow, newCol});
                                grid[newRow][newCol] = '0';  // Mark as visited
                            }
                        }
                    }
                }
            }
        }
        return islandCount;
    }
}
