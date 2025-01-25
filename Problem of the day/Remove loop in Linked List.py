class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # Helper function to detect and return the loop node.
        def detectLoop(head):
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                # If slow and fast meet, there is a loop.
                if slow == fast:
                    return slow

            return None

        # Helper function to remove the loop.
        def removeLoopNode(loop_node, head):
            ptr1 = head
            ptr2 = loop_node

            # Find the start of the loop.
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            # Find the last node in the loop.
            while ptr2.next != ptr1:
                ptr2 = ptr2.next

            # Break the loop by setting the next of the last node to None.
            ptr2.next = None

        # Detect the loop node.
        loop_node = detectLoop(head)

        # If there is a loop, remove it.
        if loop_node:
            removeLoopNode(loop_node, head)

# Utility function to create a linked list with a loop (if pos > 0).
def createLinkedListWithLoop(arr, pos):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    loop_node = None

    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

        # Save the node where the loop should connect.
        if i == pos - 1:
            loop_node = curr

    # Create the loop if pos > 0.
    if pos > 0:
        curr.next = loop_node

    return head

# Utility function to check if there is a loop in the linked list.
def hasLoop(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


#{ 
 # Driver Code Starts
# driver code:


class Node:

    def __init__(self, val):
        self.next = None
        self.data = val


class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, num):
        if self.head is None:
            self.head = Node(num)
            self.tail = self.head
        else:
            self.tail.next = Node(num)
            self.tail = self.tail.next

    def isLoop(self):
        if self.head is None:
            return False

        fast = self.head.next
        slow = self.head

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def loopHere(self, position):
        if position == 0:
            return

        walk = self.head
        for _ in range(1, position):
            walk = walk.next
        self.tail.next = walk

    def length(self):
        walk = self.head
        ret = 0
        while walk:
            ret += 1
            walk = walk.next
        return ret


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = tuple(int(x) for x in input().split())
        pos = int(input())
        n = len(arr)
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)

        Solution().removeLoop(ll.head)

        if ll.isLoop() or ll.length() != n:
            print("false")
            continue
        else:
            print("true")
        print("~")

# } Driver Code Ends