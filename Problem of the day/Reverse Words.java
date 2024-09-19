//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            String s = sc.next();
            Solution obj = new Solution();
            System.out.println(obj.reverseWords(s));
            t--;
        }
    }
}

// } Driver Code Ends

class Solution {
    // Function to reverse words in a given string.
    String reverseWords(String str) {
        // Split the string by '.'
        String[] words = str.split("\\.");
        
        // Reverse the array of words
        int left = 0, right = words.length - 1;
        while (left < right) {
            // Swap the words at left and right
            String temp = words[left];
            words[left] = words[right];
            words[right] = temp;
            left++;
            right--;
        }
        
        // Join the words back together using '.' as the separator
        return String.join(".", words);
    }
}
