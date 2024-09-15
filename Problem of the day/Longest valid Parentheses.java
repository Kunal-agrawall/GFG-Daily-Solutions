//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String S = in.readLine();
            
            Solution ob = new Solution();
            System.out.println(ob.maxLength(S));
        }
    }
}
// } Driver Code Ends

class Solution{
    static int maxLength(String S){
        // Stack to store indices of '('
        Stack<Integer> stack = new Stack<>();
        // Push -1 to handle edge cases for valid substrings starting from index 0
        stack.push(-1);
        
        int maxLength = 0;
        
        // Iterate over the string
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == '('){
                // Push the index of '(' onto the stack
                stack.push(i);
            } else {
                // Pop the top of the stack when we find a ')'
                stack.pop();
                
                if(stack.isEmpty()){
                    // If the stack is empty, push the current index as a base for future valid substrings
                    stack.push(i);
                } else {
                    // Calculate the length of the current valid substring
                    maxLength = Math.max(maxLength, i - stack.peek());
                }
            }
        }
        
        return maxLength;
    }
}
