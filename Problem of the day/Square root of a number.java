//{ Driver Code Starts
import java.util.Scanner;

class SquartRoot {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            long a = sc.nextInt();
            Solution obj = new Solution();
            System.out.println(obj.floorSqrt(a));
            t--;
        }
    }
}
// } Driver Code Ends


class Solution {
    long floorSqrt(long n) {
        // Base case
        if (n == 0 || n == 1)
            return n;
        
        // Binary search variables
        long low = 1, high = n, ans = 0;
        
        // Binary search for the floor value of sqrt(n)
        while (low <= high) {
            long mid = (low + high) / 2;
            long midSq = mid * mid;
            
            // If mid^2 == n, return mid
            if (midSq == n)
                return mid;
            
            // If mid^2 < n, move to the right half
            if (midSq < n) {
                low = mid + 1;
                ans = mid;  // Update answer since mid might be the floor value
            }
            // If mid^2 > n, move to the left half
            else {
                high = mid - 1;
            }
        }
        
        // Return the answer which is the floor of sqrt(n)
        return ans;
    }
}
