//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

class GfG {
    public static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data);
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String str[] = read.readLine().trim().split(" ");
            int n = str.length;
            Node head = new Node(Integer.parseInt(str[0]));
            Node tail = head;
            for (int i = 1; i < n; i++) {
                tail.next = new Node(Integer.parseInt(str[i]));
                tail = tail.next;
            }
            Solution obj = new Solution();
            head = obj.addOne(head);
            printList(head);
        }
    }
}
// } Driver Code Ends


class Solution {
    public Node addOne(Node head) {
        // Step 1: Reverse the linked list
        head = reverseList(head);
        
        // Step 2: Add one to the reversed list
        Node temp = head;
        int carry = 1;  // We need to add 1
        
        while (temp != null) {
            int sum = temp.data + carry;
            temp.data = sum % 10;
            carry = sum / 10;
            
            // Move to the next node
            if (carry == 0) break;  // No more carry means no more addition needed
            if (temp.next == null && carry > 0) {
                temp.next = new Node(carry);  // Add a new node for the remaining carry
                break;
            }
            temp = temp.next;
        }
        
        // Step 3: Reverse the list again to restore original order
        head = reverseList(head);
        
        return head;
    }
    
    // Helper method to reverse the linked list
    private Node reverseList(Node head) {
        Node prev = null;
        Node curr = head;
        Node next = null;
        
        while (curr != null) {
            next = curr.next;  // Save the next node
            curr.next = prev;   // Reverse the link
            prev = curr;        // Move prev and curr one step forward
            curr = next;
        }
        
        return prev;
    }
}

