//{ Driver Code Starts
// Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int t = Integer.parseInt(in.readLine().trim());
        while (t-- > 0) {
            String line = in.readLine();
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

            int key = Integer.parseInt(in.readLine().trim());
            Solution ob = new Solution();
            out.println(ob.kthSmallest(arr, key));
        }
        out.flush();
    }
}

// } Driver Code Ends

class Solution {
    public static int kthSmallest(int[] arr, int k) {
        int maxElement = 1000000; // As per the constraint 1 <= arr[i] <= 10^6
        
        // Create a count array to store frequency of elements
        int[] count = new int[maxElement + 1];
        
        // Populate the count array
        for (int num : arr) {
            count[num]++;
        }
        
        // Traverse count array to find the kth smallest element
        int cumulativeCount = 0;
        for (int i = 1; i <= maxElement; i++) {
            cumulativeCount += count[i];
            if (cumulativeCount >= k) {
                return i;
            }
        }
        
        return -1; // This return should never be hit given the problem constraints
    }
}
