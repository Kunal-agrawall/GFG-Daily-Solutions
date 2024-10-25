class Solution:
    def count(self, head, key):
        # Initialize count to 0
        count = 0
        current = head
        
        # Traverse the linked list
        while current:
            # Check if current node's data matches the key
            if current.data == key:
                count += 1
            # Move to the next node
            current = current.next
            
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        key = int(data[2 * i])
        ob = Solution()
        print(ob.count(head, key))
        print("~")

# } Driver Code Ends