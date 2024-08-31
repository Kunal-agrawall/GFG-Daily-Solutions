//{ Driver Code Starts
import java.util.*;

public class GFG {
    // Function to check if v2 is a subsequence of v1
    public static boolean isSubSequence(int[] v1, int[] v2) {
        int m = v2.length;
        int n = v1.length;
        int j = 0; // For index of v2

        // Traverse v1 and v2
        for (int i = 0; i < n && j < m; i++) {
            if (v1[i] == v2[j]) {
                j++;
            }
        }
        return j == m;
    }

    // Driver code
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while (t-- > 0) {
            String[] input = sc.nextLine().split(" ");
            int[] arr = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
            int n = arr.length;
            Solution obj = new Solution();
            List<Integer> res = obj.find3Numbers(arr);
            if (!res.isEmpty() && res.size() != 3) {
                System.out.println(-1);
            } else {
                int[] resArray = res.stream().mapToInt(Integer::intValue).toArray();
                if (resArray.length == 0) {
                    System.out.println(0);
                } else if (resArray[0] < resArray[1] && resArray[1] < resArray[2] &&
                           isSubSequence(arr, resArray)) {
                    System.out.println(1);
                } else {
                    System.out.println(-1);
                }
            }
        }
        sc.close();
    }
}

// } Driver Code Ends

class Solution {
    public List<Integer> find3Numbers(int[] arr) {
        int n = arr.length;
        if (n < 3) return new ArrayList<>();

        // Arrays to store indices
        int[] smaller = new int[n];
        int[] greater = new int[n];
        
        // Initialize smaller array
        smaller[0] = -1; // No element on the left of arr[0]
        int minIndex = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] <= arr[minIndex]) {
                minIndex = i;
                smaller[i] = -1;
            } else {
                smaller[i] = minIndex;
            }
        }

        // Initialize greater array
        greater[n - 1] = -1; // No element on the right of arr[n-1]
        int maxIndex = n - 1;
        for (int j = n - 2; j >= 0; j--) {
            if (arr[j] >= arr[maxIndex]) {
                maxIndex = j;
                greater[j] = -1;
            } else {
                greater[j] = maxIndex;
            }
        }

        // Find the triplet
        for (int i = 0; i < n; i++) {
            if (smaller[i] != -1 && greater[i] != -1) {
                List<Integer> result = new ArrayList<>();
                result.add(arr[smaller[i]]);
                result.add(arr[i]);
                result.add(arr[greater[i]]);
                return result;
            }
        }

        // If no triplet is found
        return new ArrayList<>();
    }
}
