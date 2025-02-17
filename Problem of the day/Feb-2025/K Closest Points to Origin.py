#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

from heapq import heappush, heappop
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        # Push all points with their squared distance into the heap
        for x, y in points:
            dist = x**2 + y**2  # Squared Euclidean distance (avoid sqrt for efficiency)
            heappush(min_heap, (dist, [x, y]))
        
        # Extract the k smallest distance points
        result = [heappop(min_heap)[1] for _ in range(k)]
        
        return result




#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends