import heapq

class Solution:
    def getMedian(self, arr):
        min_heap = []  # Min heap for the right half
        max_heap = []  # Max heap for the left half (stored as negative values for max behavior)
        medians = []
        
        for num in arr:
            # Insert into max heap (left side) first
            heapq.heappush(max_heap, -num)
            
            # Balance: Move the largest of max_heap to min_heap
            if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            
            # Maintain size property: max_heap can have at most one extra element
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            # Compute median
            if len(max_heap) > len(min_heap):
                medians.append(-max_heap[0])
            else:
                medians.append((-max_heap[0] + min_heap[0]) / 2.0)
        
        return medians


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends