class Solution:    
    def minimumPlatform(self, arr, dep):
        n = len(arr)
        
        # Sorting arrival and departure times separately
        arr.sort()
        dep.sort()
        
        # Pointers for arrivals and departures
        i, j = 0, 0
        platforms_needed = 0
        max_platforms = 0
        
        # Process all events in sorted order
        while i < n and j < n:
            if arr[i] <= dep[j]:  # A train is arriving
                platforms_needed += 1
                max_platforms = max(max_platforms, platforms_needed)
                i += 1
            else:  # A train is departing
                platforms_needed -= 1
                j += 1
        
        return max_platforms


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends