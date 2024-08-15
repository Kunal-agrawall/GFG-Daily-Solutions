//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class Driver
{
    public static void main(String args[])throws IOException
    {
        //reading input using BufferedReader class
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        
        //reading total testcases
        int t = Integer.parseInt(read.readLine());
        
        while(t-- > 0)
        {
            //reading length of line segment
            int n = Integer.parseInt(read.readLine().trim());
            
            
            //reading 3 segment lengths
            String str[] = read.readLine().trim().split(" ");
            
            int x = Integer.parseInt(str[0]);
            int y = Integer.parseInt(str[1]);
            int z = Integer.parseInt(str[2]);
            
            
            //calling method maximizeCuts() of class Solution()
            //and printinting the result
            System.out.println(new Solution().maximizeCuts(n, x, y, z));
        }
    }
}

// } Driver Code Ends


class Solution
{
    // Function to find the maximum number of cuts.
    public int maximizeCuts(int n, int x, int y, int z)
    {
        // Create a DP array of size n+1
        int[] dp = new int[n+1];
        
        // Initialize the array with -1 to indicate uncalculated states
        for (int i = 0; i <= n; i++) {
            dp[i] = -1;
        }
        
        // Base case: No segment, so no cuts
        dp[0] = 0;
        
        // Fill the dp array
        for (int i = 1; i <= n; i++) {
            // Check if we can make a cut of length x
            if (i >= x && dp[i-x] != -1) {
                dp[i] = Math.max(dp[i], dp[i-x] + 1);
            }
            // Check if we can make a cut of length y
            if (i >= y && dp[i-y] != -1) {
                dp[i] = Math.max(dp[i], dp[i-y] + 1);
            }
            // Check if we can make a cut of length z
            if (i >= z && dp[i-z] != -1) {
                dp[i] = Math.max(dp[i], dp[i-z] + 1);
            }
        }
        
        // If dp[n] is still -1, return 0, meaning no cuts can be made
        return dp[n] == -1 ? 0 : dp[n];
    }
}
