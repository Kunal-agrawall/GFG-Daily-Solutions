//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine().trim());
        while (t-- > 0) {
            String A[] = in.readLine().trim().split(" ");
            int N = Integer.parseInt(A[0]);
            A = in.readLine().trim().split(" ");

            Solution ob = new Solution();
            System.out.println(ob.isCircle(A));
        }
    }
}
// } Driver Code Ends

class Solution {
    
    // Method to check if the strings can form a circle
    public int isCircle(String arr[]) {
        // Total number of strings
        int n = arr.length;
        
        // Step 1: Create indegree and outdegree arrays
        int[] inDegree = new int[26];
        int[] outDegree = new int[26];
        
        // Adjacency list to store the graph (char to char mapping)
        Map<Character, List<Character>> graph = new HashMap<>();
        
        // Step 2: Build the graph and calculate in and out degrees
        for (String word : arr) {
            char start = word.charAt(0);  // first character of the string
            char end = word.charAt(word.length() - 1);  // last character of the string
            
            // Increment the outDegree for the starting character and inDegree for the ending character
            outDegree[start - 'a']++;
            inDegree[end - 'a']++;
            
            // Create a directed edge from start to end
            graph.computeIfAbsent(start, k -> new ArrayList<>()).add(end);
        }
        
        // Step 3: Check if indegree matches outdegree for all characters
        for (int i = 0; i < 26; i++) {
            if (inDegree[i] != outDegree[i]) {
                return 0;  // not possible to form a circle
            }
        }
        
        // Step 4: Perform DFS to ensure the graph is strongly connected
        // Find a character that has an out degree > 0 to start the DFS
        char start = arr[0].charAt(0);
        Set<Character> visited = new HashSet<>();
        dfs(start, graph, visited);
        
        // Check if we have visited all nodes that have edges
        for (String word : arr) {
            if (!visited.contains(word.charAt(0))) {
                return 0;  // not fully connected
            }
        }
        
        // If all conditions are met, return 1
        return 1;
    }
    
    // DFS to explore the graph
    private void dfs(char node, Map<Character, List<Character>> graph, Set<Character> visited) {
        visited.add(node);
        if (graph.containsKey(node)) {
            for (char neighbor : graph.get(node)) {
                if (!visited.contains(neighbor)) {
                    dfs(neighbor, graph, visited);
                }
            }
        }
    }
}
