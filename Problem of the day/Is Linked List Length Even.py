class Solution:
    def isLengthEven(self, head):
        # Initialize a counter for nodes
        count = 0
        
        # Traverse the linked list
        current = head
        while current:
            count += 1  # Increment the counter for each node
            current = current.next  # Move to the next node
        
        # Check if the count is even
        return count % 2 == 0


#{ 
 # Driver Code Starts
#main


class Node:
    # Constructor to initialize the node object
    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def _init_(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if _name_ == '_main_':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        flag = Solution().isLengthEven(llist.head)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
        t -= 1
# Contributed by: Harshit Sidhwa

# } Driver Code Ends