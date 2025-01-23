class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Initialize two pointers, slow and fast.
        slow = head
        fast = head

        # Traverse the linked list.
        while fast and fast.next:
            # Move slow by one step.
            slow = slow.next
            # Move fast by two steps.
            fast = fast.next.next

            # Check if slow and fast meet.
            if slow == fast:
                return True  # Loop detected.

        # If we reach here, no loop exists.
        return False




#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    #connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))
        res = Solution().detectLoop(LL.head)
        if (res):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends