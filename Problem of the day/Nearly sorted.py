import heapq

class Solution:
    def nearlySorted(self, arr, k):
        # Initialize a min-heap
        min_heap = []
        
        # Push the first k + 1 elements into the min-heap
        for i in range(min(k + 1, len(arr))):
            heapq.heappush(min_heap, arr[i])
        
        # Index for placing sorted elements in the array
        index = 0
        
        # Process the remaining elements in the array
        for i in range(k + 1, len(arr)):
            # Pop the smallest element from the heap and place it in the array
            arr[index] = heapq.heappop(min_heap)
            index += 1
            
            # Push the next element into the heap
            heapq.heappush(min_heap, arr[i])
        
        # Empty the remaining elements from the heap
        while min_heap:
            arr[index] = heapq.heappop(min_heap)
            index += 1




#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if _name_ == "_main_":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends