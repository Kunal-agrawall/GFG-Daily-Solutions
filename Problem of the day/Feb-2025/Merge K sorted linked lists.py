from heapq import heappush, heappop

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    # This allows Node objects to be compared in the heap
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def mergeKLists(self, arr):
        # Min-heap to store (node value, index, node) tuples
        heap = []
        
        # Push the first node of each linked list into the heap
        for node in arr:
            if node:
                heappush(heap, (node.data, id(node), node))
        
        # Dummy node to keep track of the head of the merged list
        dummy = Node(0)
        curr = dummy
        
        while heap:
            # Extract the smallest node
            _, _, node = heappop(heap)
            curr.next = node
            curr = curr.next

            # Push the next node of the extracted node into the heap
            if node.next:
                heappush(heap, (node.next.data, id(node.next), node.next))

        return dummy.next


#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends