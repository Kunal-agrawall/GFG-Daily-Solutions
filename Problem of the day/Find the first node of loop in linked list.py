class Solution:
    def findFirstNode(self, head):
        # Step 1: Detect the loop using Floyd's Cycle Detection Algorithm
        slow = head
        fast = head
        has_loop = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                has_loop = True
                break
        
        # If no loop is detected, return None
        if not has_loop:
            return None
        
        # Step 2: Find the starting node of the loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # This is the first node in the loop



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, tail, position):
    if position == 0:
        return

    walk = head
    for _ in range(1, position):
        walk = walk.next
    tail.next = walk


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, tail, k)

        ob = Solution()
        ans = ob.findFirstNode(head)
        if (ans == None):
            print(-1)
        else:
            print(ans.data)
        print("~")

# } Driver Code Ends