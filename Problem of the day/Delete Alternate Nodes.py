class Solution:
    def deleteAlt(self, head):
        # If the list is empty or has only one node, return the head as is
        if not head or not head.next:
            return head
        
        # Initialize current node as the head
        current = head
        
        # Traverse the list
        while current and current.next:
            # Skip the next node (even position)
            current.next = current.next.next
            # Move to the next node (which is an odd position after deletion)
            current = current.next
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        ob = Solution()
        ob.deleteAlt(head)
        printList(head)

# } Driver Code Ends