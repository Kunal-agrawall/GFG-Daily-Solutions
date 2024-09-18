//{ Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class Driverclass
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        
        //Reading total number of testcases
        int t= sc.nextInt();
        
        while(t-- >0)
        {
            //reading the string
            String st = sc.next();
            
            //calling ispar method of Paranthesis class 
            //and printing "balanced" if it returns true
            //else printing "not balanced"
            if(new Solution().ispar(st) == true)
                System.out.println("balanced");
            else
                System.out.println("not balanced");
        
        }
    }
}
// } Driver Code Ends

class Solution
{
    // Function to check if brackets are balanced or not.
    static boolean ispar(String x)
    {
        // Stack to store opening brackets
        Stack<Character> stack = new Stack<>();

        // Traverse the string
        for (int i = 0; i < x.length(); i++) {
            char ch = x.charAt(i);

            // If it's an opening bracket, push it to the stack
            if (ch == '{' || ch == '(' || ch == '[') {
                stack.push(ch);
            }
            // If it's a closing bracket
            else if (ch == '}' || ch == ')' || ch == ']') {
                // If stack is empty, no matching opening bracket
                if (stack.isEmpty()) {
                    return false;
                }

                // Pop the top element and check if it matches the corresponding opening bracket
                char top = stack.pop();
                if (!isMatchingPair(top, ch)) {
                    return false;
                }
            }
        }

        // If the stack is empty, all brackets were matched, otherwise not balanced
        return stack.isEmpty();
    }

    // Helper function to check if the pair of brackets match
    static boolean isMatchingPair(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '{' && close == '}') ||
               (open == '[' && close == ']');
    }
}
