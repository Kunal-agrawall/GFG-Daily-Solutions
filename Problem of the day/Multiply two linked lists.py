class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    MOD = 10**9 + 7  # We will use this modulo for the final result
    
    def multiply_two_lists(self, first, second):
        # Initialize numbers to 0
        num1 = 0
        num2 = 0
        
        # Traverse the first list and form the number
        while first:
            num1 = (num1 * 10 + first.data) % self.MOD
            first = first.next
        
        # Traverse the second list and form the number
        while second:
            num2 = (num2 * 10 + second.data) % self.MOD
            second = second.next
        
        # Multiply the two numbers and return the result modulo MOD
        return (num1 * num2) % self.MOD



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def new_node(data):
    return Node(data)


def push(head_ref, new_data):
    new_Node = new_node(new_data)
    new_Node.next = head_ref[0]
    head_ref[0] = new_Node


def reverse(r):
    prev = None
    cur = r[0]
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    r[0] = prev


def free_list(Node):
    while Node:
        temp = Node
        Node = Node.next
        del temp


def print_list(Node):
    while Node:
        print(Node.data, end=" ")
        Node = Node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        first, second = [None], [None]
        arr = list(map(int, input().split()))
        for num in arr:
            push(first, num)

        brr = list(map(int, input().split()))
        for num in brr:
            push(second, num)

        reverse(first)
        reverse(second)

        ob = Solution()
        res = ob.multiply_two_lists(first[0], second[0])
        print(res)

# } Driver Code Ends