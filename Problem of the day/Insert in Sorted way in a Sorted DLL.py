class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        # Creating the new node to insert
        new_node = Node(x)
        
        # Case 1: Empty list, the new node becomes the head
        if head is None:
            return new_node
        
        # Case 2: Insert at the beginning if `x` is smaller than the head's data
        if x < head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        
        # Case 3: Traverse the list to find the insertion point
        current = head
        while current.next is not None and current.next.data < x:
            current = current.next
        
        # Case 4: Insert the node in the middle or at the end of the list
        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
        
        return head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends