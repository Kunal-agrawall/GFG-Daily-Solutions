//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int[][] grid = new int[n][n];
            for(int i = 0; i < n; i++){
                String[] S = br.readLine().trim().split(" ");
                for(int j = 0; j < n; j++){
                    grid[i][j] = Integer.parseInt(S[j]);
                }
            }
            Solution obj = new Solution();
            int ans = obj.minimumCostPath(grid);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends

class Solution {
    // Direction vectors for moving up, down, left, and right
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public int minimumCostPath(int[][] grid) {
        int n = grid.length;
        int[][] dist = new int[n][n];

        // Initialize distances with a large value
        for (int[] row : dist) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        // Min-heap (priority queue) to store cells to explore, initialized with the top-left cell
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        pq.add(new int[]{0, 0, grid[0][0]});
        dist[0][0] = grid[0][0];

        // While there are cells to explore
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int x = current[0];
            int y = current[1];
            int currDist = current[2];

            // If we reached the bottom-right corner, return the distance
            if (x == n - 1 && y == n - 1) {
                return currDist;
            }

            // Explore the 4 possible directions
            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                // Check if the new position is within bounds
                if (newX >= 0 && newX < n && newY >= 0 && newY < n) {
                    int newDist = currDist + grid[newX][newY];

                    // If a shorter path to the neighbor is found
                    if (newDist < dist[newX][newY]) {
                        dist[newX][newY] = newDist;
                        pq.add(new int[]{newX, newY, newDist});
                    }
                }
            }
        }

        // This point should not be reached
        return -1;
    }
}
