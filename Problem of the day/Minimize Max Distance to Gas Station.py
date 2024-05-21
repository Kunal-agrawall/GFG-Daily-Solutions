#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findSmallestMaxDist(self, stations, k):
        def possible(d):
            count = 0
            for i in range(len(stations) - 1):
                dist = stations[i + 1] - stations[i]
                count += int(dist / d)
            return count <= k

        left, right = 0, stations[-1] - stations[0]
        
        while right - left > 1e-6:
            mid = (left + right) / 2.0
            if possible(mid):
                right = mid
            else:
                left = mid
        
        return round(right, 2)

# Example usage:
solution = Solution()
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9


#{ 
 # Driver Code Starts.
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends