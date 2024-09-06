//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim()); // Inputting the testcases
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

            Solution obj = new Solution();

            // calling maxSubarraySum() function
            System.out.println(obj.maxSubarraySum(arr));
        }
    }
}

// } Driver Code Ends

class Solution {
    // Function to find the sum of contiguous subarray with the maximum sum.
    int maxSubarraySum(int[] arr) {
        // Initialize maxSum with the smallest integer value and currentSum as 0.
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;

        for (int i = 0; i < arr.length; i++) {
            // Add current element to currentSum.
            currentSum += arr[i];
            
            // Update maxSum if the currentSum is greater.
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }

            // If currentSum drops below 0, reset it to 0 (start a new subarray).
            if (currentSum < 0) {
                currentSum = 0;
            }
        }

        return maxSum;
    }
}
