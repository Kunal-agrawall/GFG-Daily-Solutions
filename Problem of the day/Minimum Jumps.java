//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String line = br.readLine();
            String[] tokens = line.split(" ");

            // Create an ArrayList to store the integers
            ArrayList<Integer> array = new ArrayList<>();

            // Parse the tokens into integers and add to the array
            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;

            System.out.println(new Solution().minJumps(arr));
            // System.out.println("~");
        }
    }
}

// } Driver Code Ends

class Solution {
    static int minJumps(int[] arr) {
        if (arr.length <= 1) return 0;  // If already at the last index
        
        if (arr[0] == 0) return -1;     // If the first element is 0, we cannot make any move

        int maxReach = arr[0];  // The farthest we can reach
        int steps = arr[0];     // Steps we can still take
        int jumps = 1;          // We need at least one jump initially
        
        // Traverse the array
        for (int i = 1; i < arr.length; i++) {
            if (i == arr.length - 1) return jumps;  // We have reached the end
            
            maxReach = Math.max(maxReach, i + arr[i]);  // Update the max reachable index
            steps--;  // Decrease step count

            if (steps == 0) {
                // If no more steps are left, we must make a jump
                jumps++;
                
                // If we can't move further, return -1
                if (i >= maxReach) return -1;

                // Reset steps to the number of steps to reach maxReach from current index
                steps = maxReach - i;
            }
        }

        return -1;  // If we exit the loop without having reached the end
    }
}
