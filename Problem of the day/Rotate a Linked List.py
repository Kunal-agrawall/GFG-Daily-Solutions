class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Calculate the length of the linked list.
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Modulo k by the length to handle cases where k >= length.
        k = k % length
        if k == 0:
            return head

        # Connect the last node to the head to form a circular linked list.
        current.next = head

        # Find the new head after k rotations.
        steps_to_new_head = k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        # Break the circle and set the new head.
        new_head = new_tail.next
        new_tail.next = None

        return new_head

# Helper function to create a linked list from a list of values.
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values.
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        print("~")
        t -= 1

# } Driver Code Ends