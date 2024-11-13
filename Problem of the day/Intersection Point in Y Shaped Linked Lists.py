def intersetPoint(head1, head2):
    # Initialize two pointers to the heads of each linked list
    ptr1, ptr2 = head1, head2

    # Traverse until both pointers are the same
    while ptr1 != ptr2:
        # Move each pointer one step, or redirect it to the start of the other list if it reaches the end
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1

    # If there is an intersection, ptr1 (or ptr2) will point to the intersecting node
    # If there is no intersection, both will be None when they reach the end
    return ptr1.data if ptr1 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(INPUT_LINES).next_
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys._stdout_.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:

    def _init_(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:

    def _init_(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if _name_ == '_main_':
    t = int(input())
    for cases in range(t):

        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(
                    node
                )  # add to the end of the list b, only the intersection

        print(intersetPoint(a.head, b.head))

        print("~")

# } Driver Code Ends