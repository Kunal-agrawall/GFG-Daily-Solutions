//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner ob = new Scanner(System.in);
        int t = ob.nextInt();
        while (t-- > 0) {
            long n = ob.nextLong();
            Solution ab = new Solution();
            long k = ab.findNth(n);
            System.out.println(k);
        }
    }
}

// } Driver Code Ends

class Solution {
    long findNth(long n) {
        long result = 0;
        long multiplier = 1;

        // Convert the number to base-9
        while (n > 0) {
            result += (n % 9) * multiplier;
            n /= 9;
            multiplier *= 10;
        }

        return result;
    }
}
