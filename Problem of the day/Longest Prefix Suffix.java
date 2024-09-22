//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {

            String s = read.readLine();
            Solution ob = new Solution();
            System.out.println(ob.lps(s));
        }
    }
}
// } Driver Code Ends

class Solution {
    int lps(String str) {
        int n = str.length();
        
        // lps array to store the longest prefix suffix lengths
        int[] lps = new int[n];
        
        // Length of the previous longest prefix suffix
        int len = 0;
        int i = 1;
        
        // Initialize the lps[0] to 0 as the single character string has no proper prefix or suffix
        lps[0] = 0;
        
        // Build the lps array
        while (i < n) {
            if (str.charAt(i) == str.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        
        // The longest proper prefix which is also a suffix is stored in lps[n-1]
        return lps[n - 1];
    }
}
