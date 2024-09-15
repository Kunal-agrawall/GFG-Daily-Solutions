//{ Driver Code Starts
//Initial Template for Java

import java.util.Scanner;
import java.util.*;
import java.io.*;
import java.lang.*;

class Node
{
	Node left, right;
	int data;
	
	Node(int d)
	{
		data = d;
		left = right = null;
	}
	
}
class BT_To_DLL
{
    
    static Node buildTree(String str)throws IOException{
        
        if(str.length()==0 || str.charAt(0)=='N'){
            return null;
        }
        
        String ip[] = str.split(" ");
        // Create the root of the tree
        Node root = new Node(Integer.parseInt(ip[0]));
        // Push the root to the queue
        
        Queue<Node> queue = new LinkedList<>(); 
        
        queue.add(root);
        // Starting from the second element
        
        int i = 1;
        while(queue.size()>0 && i < ip.length) {
            
            // Get and remove the front of the queue
            Node currNode = queue.peek();
            queue.remove();
                
            // Get the current node's value from the string
            String currVal = ip[i];
                
            // If the left child is not null
            if(!currVal.equals("N")) {
                    
                // Create the left child for the current node
                currNode.left = new Node(Integer.parseInt(currVal));
                // Push it to the queue
                queue.add(currNode.left);
            }
                
            // For the right child
            i++;
            if(i >= ip.length)
                break;
                
            currVal = ip[i];
                
            // If the right child is not null
            if(!currVal.equals("N")) {
                    
                // Create the right child for the current node
                currNode.right = new Node(Integer.parseInt(currVal));
                    
                // Push it to the queue
                queue.add(currNode.right);
            }
            i++;
        }
        
        return root;
    }
    

	void inorder(Node node)
	{
		if(node==null)
			return ;
		else
			inorder(node.left);
			System.out.print(node.data + " ");
			inorder(node.right);
	}
	public static void printList(Node head) 
    {
		Node prev = head;
        while (head != null) 
        {
            System.out.print(head.data + " ");
			prev = head;
            head = head.right;
        }
		
		System.out.println();
		while(prev != null)
		{
			System.out.print(prev.data+" ");
			prev = prev.left;
		}
    }
	public static void main(String args[])  throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        
	        int t=Integer.parseInt(br.readLine());
    
	        while(t > 0){
	            String s = br.readLine();
    	    	Node root = buildTree(s);
        	    Solution g = new Solution();
			    
			    Node ans = g.bToDLL(root);
			    printList(ans);
                t--;
                System.out.println();
	        }
			
		
	}
}

// } Driver Code Ends

class Solution {
    // Pointer to store the head of the DLL
    Node head = null;
    
    // Pointer to store the previously processed node
    Node prev = null;

    // Function to convert binary tree to doubly linked list and return it.
    Node bToDLL(Node root) {
        // Base case
        if (root == null) {
            return null;
        }

        // Recursively convert the left subtree
        bToDLL(root.left);
        
        // Now convert this node
        if (prev == null) {
            // This node (root) is the leftmost node, so set it as head
            head = root;
        } else {
            // Link the previous node (prev) with the current node (root)
            prev.right = root;
            root.left = prev;
        }
        
        // Mark this node as the previous node for the next iteration
        prev = root;
        
        // Recursively convert the right subtree
        bToDLL(root.right);
        
        return head;
    }
}
