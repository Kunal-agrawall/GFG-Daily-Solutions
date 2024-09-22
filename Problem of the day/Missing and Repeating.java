//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    // Driver code
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String[] str = br.readLine().split(" ");

            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(str[i]);
            }

            int[] ans = new Solve().findTwoElement(a);
            System.out.println(ans[0] + " " + ans[1]);
        }
    }
}
// } Driver Code Ends

class Solve {
    int[] findTwoElement(int arr[]) {
        int n = arr.length;
        long S = (long) n * (n + 1) / 2; // Sum of first n natural numbers
        long S2 = (long) n * (n + 1) * (2 * n + 1) / 6; // Sum of squares of first n natural numbers

        long S1 = 0, S3 = 0;
        
        // Calculate actual sum and sum of squares from the array
        for (int i = 0; i < n; i++) {
            S1 += arr[i];
            S3 += (long) arr[i] * arr[i];
        }

        long diff = S1 - S;         // B - A
        long squareDiff = S3 - S2;  // B^2 - A^2

        // From the equation B^2 - A^2 = (B + A)(B - A)
        long sum = squareDiff / diff;  // B + A

        int B = (int) (diff + sum) / 2;
        int A = (int) sum - B;

        return new int[]{B, A};
    }
}
