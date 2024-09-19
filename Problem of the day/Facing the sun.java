//{ Driver Code Starts
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // consume the remaining newline
        while (t-- > 0) {
            String input = sc.nextLine();
            String[] inputStrings = input.split(" ");
            int[] height = new int[inputStrings.length];
            for (int i = 0; i < inputStrings.length; i++) {
                height[i] = Integer.parseInt(inputStrings[i]);
            }
            Solution ob = new Solution();
            int ans = ob.countBuildings(height);
            System.out.println(ans);
        }
        sc.close();
    }
}

// } Driver Code Ends

class Solution {
    // Returns count of buildings that can see the sunlight
    public int countBuildings(int[] height) {
        int count = 0;
        int max_height = 0;
        
        // Traverse the buildings
        for (int i = 0; i < height.length; i++) {
            // If the current building is taller than all previous buildings
            if (height[i] > max_height) {
                count++;  // This building can see the sunrise
                max_height = height[i];  // Update the max height seen so far
            }
        }
        
        return count;
    }
}
