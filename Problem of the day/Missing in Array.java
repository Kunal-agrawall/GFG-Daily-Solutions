//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String[] str = br.readLine().trim().split(" ");
            int[] arr = new int[n - 1];
            for (int i = 0; i < n - 1; i++) {
                arr[i] = Integer.parseInt(str[i]);
            }
            Solution sln = new Solution();
            System.out.println(sln.missingNumber(n, arr));
        }
    }
}
// } Driver Code Ends

class Solution {

    // Note that the size of the array is n-1
    int missingNumber(int n, int arr[]) {
        // Step 1: Calculate the expected sum of numbers from 1 to n
        int totalSum = n * (n + 1) / 2;

        // Step 2: Calculate the sum of the elements in the array
        int arrSum = 0;
        for (int num : arr) {
            arrSum += num;
        }

        // Step 3: The missing number is the difference between the total sum and the array sum
        return totalSum - arrSum;
    }
}