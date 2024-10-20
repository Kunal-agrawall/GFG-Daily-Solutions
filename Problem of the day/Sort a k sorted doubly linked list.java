//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class DLLNode {
    int data;
    DLLNode next;
    DLLNode prev;

    DLLNode(int val) {
        data = val;
        next = null;
        prev = null;
    }
}

public class Main {
    public static void push(DLLNode tail, int new_data) {
        DLLNode newNode = new DLLNode(new_data);
        newNode.next = null;
        newNode.prev = tail;

        if (tail != null) {
            tail.next = newNode;
        }
    }

    public static void printList(DLLNode head) {
        if (head == null) {
            return;
        }

        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            String[] arr = br.readLine().trim().split(" ");
            int k = Integer.parseInt(br.readLine().trim());

            DLLNode head = new DLLNode(Integer.parseInt(arr[0]));
            DLLNode tail = head;

            for (int i = 1; i < arr.length; i++) {
                push(tail, Integer.parseInt(arr[i]));
                tail = tail.next;
            }

            Solution obj = new Solution();
            DLLNode sorted_head = obj.sortAKSortedDLL(head, k);
            printList(sorted_head);
        }
    }
}

// } Driver Code Ends

class Solution {
    public DLLNode sortAKSortedDLL(DLLNode head, int k) {
        if (head == null || head.next == null) {
            return head; // The list is already sorted if it's empty or has one element
        }
        
        // Min-heap (Priority Queue) to store DLL nodes by their data values
        PriorityQueue<DLLNode> minHeap = new PriorityQueue<>((a, b) -> a.data - b.data);
        
        DLLNode newHead = null, last = null;
        
        // Step 1: Insert first k+1 elements into the min-heap
        DLLNode current = head;
        for (int i = 0; i <= k && current != null; i++) {
            minHeap.add(current);
            current = current.next;
        }
        
        // Step 2: Process the list, reconstructing it in sorted order
        while (!minHeap.isEmpty()) {
            // Extract the smallest element from the heap
            DLLNode smallest = minHeap.poll();
            
            // If this is the first node, it's the new head
            if (newHead == null) {
                newHead = smallest;
                smallest.prev = null;
                last = newHead; // 'last' keeps track of the end of the sorted part of the list
            } else {
                // Append the smallest node to the sorted list
                last.next = smallest;
                smallest.prev = last;
                last = smallest;
            }
            
            // Step 3: Add the next node from the unsorted part to the heap
            if (current != null) {
                minHeap.add(current);
                current = current.next;
            }
        }
        
        // Make sure the last node points to null
        last.next = null;
        
        return newHead;
    }
}
