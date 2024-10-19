//{ Driver Code Starts
// Initial Template for Java

// Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;


// } Driver Code Ends

class Solution {

    String roundToNearest(String str) {
        int n = str.length();
        // Get the last digit of the number
        int lastDigit = str.charAt(n - 1) - '0';
        
        // If the last digit is less than or equal to 5, we round down (replace it with '0')
        if (lastDigit <= 5) {
            return str.substring(0, n - 1) + "0";
        } else {
            // If last digit is greater than 5, we need to round up
            StringBuilder sb = new StringBuilder(str.substring(0, n - 1));
            int i = n - 2;

            // Carry logic to handle numbers like 999 -> 1000
            while (i >= 0 && sb.charAt(i) == '9') {
                sb.setCharAt(i, '0');
                i--;
            }

            if (i == -1) {
                // If all the digits were 9s, prepend '1' to the result
                sb.insert(0, '1');
            } else {
                // Otherwise, increment the current digit
                sb.setCharAt(i, (char)(sb.charAt(i) + 1));
            }

            // Append the '0' as the last digit
            sb.append('0');
            return sb.toString();
        }
    }
}



//{ Driver Code Starts.

// Driver class
class Array {

    // Driver code
    public static void main(String[] args) throws IOException {
        // Taking input using buffered reader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testcases = Integer.parseInt(br.readLine());

        // looping through all testcases
        while (testcases-- > 0) {

            String str = br.readLine().trim();

            Solution obj = new Solution();

            String res = obj.roundToNearest(str);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends