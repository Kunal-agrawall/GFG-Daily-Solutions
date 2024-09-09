//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String input = br.readLine();
            String[] inputArray = input.split("\\s+");
            ArrayList<Integer> a = new ArrayList<>();

            for (String s : inputArray) {
                a.add(Integer.parseInt(s));
            }

            Solution ob = new Solution();
            ob.sort012(a);

            for (int num : a) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends

class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    public void sort012(ArrayList<Integer> arr) {
        int low = 0, mid = 0, high = arr.size() - 1;

        // Process all elements in the array
        while (mid <= high) {
            switch (arr.get(mid)) {
                // If the element is 0
                case 0: {
                    swap(arr, low, mid);
                    low++;
                    mid++;
                    break;
                }
                // If the element is 1
                case 1: {
                    mid++;
                    break;
                }
                // If the element is 2
                case 2: {
                    swap(arr, mid, high);
                    high--;
                    break;
                }
            }
        }
    }

    // Helper function to swap two elements in the array
    private void swap(ArrayList<Integer> arr, int i, int j) {
        int temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }
}
