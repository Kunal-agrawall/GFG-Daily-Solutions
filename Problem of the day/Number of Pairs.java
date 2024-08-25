//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int g = 0; g < t; g++) {
            String[] str = (br.readLine()).trim().split(" ");
            int x[] = new int[str.length];
            for (int i = 0; i < str.length; i++) x[i] = Integer.parseInt(str[i]);
            str = (br.readLine()).trim().split(" ");
            int[] y = new int[str.length];
            for (int i = 0; i < str.length; i++) {
                y[i] = Integer.parseInt(str[i]);
            }
            System.out.println(new Solution().countPairs(x, y, x.length, y.length));
        }
    }
}

// } Driver Code Ends

class Solution {
    // Function to count number of pairs such that x^y is greater than y^x.
    public long countPairs(int x[], int y[], int M, int N) {
        // Sort array y for binary search
        Arrays.sort(y);

        // Array to store counts of elements 0, 1, 2, 3, and 4 in y.
        int[] count = new int[5];
        for (int i = 0; i < N; i++) {
            if (y[i] < 5) {
                count[y[i]]++;
            }
        }

        long totalPairs = 0;

        // Traverse through all elements of x
        for (int i = 0; i < M; i++) {
            totalPairs += countValidPairs(x[i], y, count, N);
        }

        return totalPairs;
    }

    // Function to count number of pairs with a particular element x in array x[]
    public long countValidPairs(int x, int y[], int count[], int N) {
        // If x is 0, then no pair (x, y) can satisfy x^y > y^x
        if (x == 0) return 0;

        // If x is 1, then only pairs with y = 0 can satisfy x^y > y^x
        if (x == 1) return count[0];

        // Count the number of elements in y[] greater than x using binary search
        int idx = Arrays.binarySearch(y, x);
        if (idx < 0) {
            idx = -(idx + 1);
        } else {
            while (idx < N && y[idx] == x) idx++;
        }
        long countPairs = N - idx;

        // Adjust count for special cases
        countPairs += count[0] + count[1];

        // If x == 2, reduce the count of pairs for y = 3 and y = 4
        if (x == 2) countPairs -= (count[3] + count[4]);

        // If x == 3, add the count of pairs for y = 2
        if (x == 3) countPairs += count[2];

        return countPairs;
    }
}
