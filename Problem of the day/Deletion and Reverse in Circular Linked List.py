class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if not head or head.next == head:
            return head  # Empty list or single node list doesn't need reversal
        
        prev = None
        curr = head
        next_node = None
        first_node = head
        
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == head:  # Once we've gone around the circle
                break

        # After the loop, curr is back at head, and prev is at the last node
        first_node.next = prev  # The first node (previous head) now points to the last node
        head = prev  # Update the head pointer to the new head (previous last node)
        
        return head
    
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if not head:
            return None
        
        curr = head
        prev = None
        
        # Case 1: If the list contains only one node
        if head.data == key and head.next == head:
            return None  # Only node in the list, so return None
        
        # Case 2: If the head node is to be deleted
        if head.data == key:
            # Find the last node to adjust its next pointer to the new head
            last = head
            while last.next != head:
                last = last.next
            # Update the head and last node's next pointer
            head = head.next
            last.next = head
            return head
        
        # Case 3: Delete any node other than head
        while curr.next != head:
            if curr.data == key:
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next
        
        # Finally, check if the last node needs to be deleted
        if curr.data == key:
            prev.next = curr.next
        
        return head

        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends