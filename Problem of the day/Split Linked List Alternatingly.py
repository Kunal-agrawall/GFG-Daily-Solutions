class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        if not head:
            return [None, None]
        
        # Initialize the two sublist heads and their respective tail pointers
        list1_head = None
        list2_head = None
        list1_tail = None
        list2_tail = None
        
        current = head
        toggle = True  # Toggle to switch between list1 and list2
        
        # Traverse the linked list
        while current:
            if toggle:
                # Add to list1
                if list1_head is None:
                    list1_head = current
                    list1_tail = current
                else:
                    list1_tail.next = current
                    list1_tail = list1_tail.next
            else:
                # Add to list2
                if list2_head is None:
                    list2_head = current
                    list2_tail = current
                else:
                    list2_tail.next = current
                    list2_tail = list2_tail.next
            
            # Move to the next node and toggle the list
            current = current.next
            toggle = not toggle
        
        # End the two lists
        if list1_tail:
            list1_tail.next = None
        if list2_tail:
            list2_tail.next = None
        
        return [list1_head, list2_head]



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends