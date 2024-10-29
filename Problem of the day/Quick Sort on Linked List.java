//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int key) {
        data = key;
        next = null;
    }
}

class SortLL {
    static Node head;

    public static void main(String[] args) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {
            String str[] = read.readLine().trim().split(" ");
            int n = str.length;
            Node head = new Node(Integer.parseInt(str[0]));
            addToTheLast(head);

            for (int i = 1; i < n; i++) {
                int a = Integer.parseInt(str[i]);
                addToTheLast(new Node(a));
            }

            GfG gfg = new GfG();
            Node node = gfg.quickSort(head);

            printList(node);
            System.out.println();
        
System.out.println("~");
}
    }

    public static void printList(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }

    public static void addToTheLast(Node node) {
        if (head == null) {
            head = node;
        } else {
            Node temp = head;
            while (temp.next != null) temp = temp.next;
            temp.next = node;
        }
    }
}
// } Driver Code Ends

class GfG {
    
    // Function to sort the linked list using quicksort
    public static Node quickSort(Node head) {
        // Base case: if the list is empty or has a single element
        if (head == null || head.next == null) {
            return head;
        }
        
        // Partition the list around a pivot (last node in this case)
        Node[] partitioned = partition(head);
        
        // Recursively sort the less and greater lists
        Node leftSorted = quickSort(partitioned[0]);
        Node rightSorted = quickSort(partitioned[2]);
        
        // Concatenate the sorted less list, equal list (pivot), and sorted greater list
        return concatenate(leftSorted, partitioned[1], rightSorted);
    }
    
    // Partition the list and return three parts: less than pivot, pivot itself, and greater than pivot
    private static Node[] partition(Node head) {
        Node lessHead = new Node(0), lessTail = lessHead;
        Node equalHead = new Node(0), equalTail = equalHead;
        Node greaterHead = new Node(0), greaterTail = greaterHead;
        
        // Use the last node as pivot
        Node pivot = getTail(head);
        Node curr = head;
        
        // Partition the list into less, equal, and greater lists
        while (curr != null) {
            if (curr.data < pivot.data) {
                lessTail.next = curr;
                lessTail = curr;
            } else if (curr.data == pivot.data) {
                equalTail.next = curr;
                equalTail = curr;
            } else {
                greaterTail.next = curr;
                greaterTail = curr;
            }
            curr = curr.next;
        }
        
        // Mark the ends of the partitions to avoid cycles
        lessTail.next = null;
        equalTail.next = null;
        greaterTail.next = null;
        
        return new Node[] { lessHead.next, equalHead.next, greaterHead.next };
    }
    
    // Concatenate less, pivot, and greater parts
    private static Node concatenate(Node less, Node equal, Node greater) {
        Node dummyHead = new Node(0), tail = dummyHead;
        
        // Attach the less partition
        tail.next = less;
        tail = getTail(tail);  // Move to the end of the less list
        
        // Attach the equal (pivot) partition
        tail.next = equal;
        tail = getTail(tail);  // Move to the end of the equal list
        
        // Attach the greater partition
        tail.next = greater;
        
        return dummyHead.next;
    }
    
    // Helper to find the tail of the list
    private static Node getTail(Node node) {
        while (node != null && node.next != null) {
            node = node.next;
        }
        return node;
    }
}
