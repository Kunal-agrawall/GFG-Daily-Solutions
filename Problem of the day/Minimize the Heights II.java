//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int k = Integer.parseInt(inputLine[0]);

            // Ensure input is read correctly
            inputLine = br.readLine().trim().split(" ");
            if (inputLine == null || inputLine.length == 0) {
                System.out.println("Invalid input");
                continue;
            }

            int[] arr = new int[inputLine.length];
            for (int i = 0; i < inputLine.length; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            int ans = new Solution().getMinDiff(arr, k);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends

class Solution {
    int getMinDiff(int[] arr, int k) {
        // Sort the array to make comparison easier
        Arrays.sort(arr);
        int n = arr.length;
        
        // Initialize the result as the difference between the maximum and minimum
        int result = arr[n - 1] - arr[0];
        
        // Variables to store the smallest and largest tower after modification
        int small = arr[0] + k;
        int large = arr[n - 1] - k;
        
        // Iterate through the array and adjust heights
        for (int i = 0; i < n - 1; i++) {
            int minHeight = Math.min(small, arr[i + 1] - k);
            int maxHeight = Math.max(large, arr[i] + k);
            
            // Update the result with the minimum difference found
            if (minHeight >= 0) {
                result = Math.min(result, maxHeight - minHeight);
            }
        }
        
        return result;
    }
}
