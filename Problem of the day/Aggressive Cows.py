class Solution:

    def aggressiveCows(self, stalls, k):
        # Sort the stalls to simplify distance calculation
        stalls.sort()
        
        # Binary search for the maximum minimum distance
        def canPlaceCows(distance):
            count, last_position = 1, stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                if count == k:
                    return True
            return False

        low, high = 1, stalls[-1] - stalls[0]
        result = 0

        while low <= high:
            mid = (low + high) // 2
            
            if canPlaceCows(mid):
                result = mid  # Store the current valid result
                low = mid + 1  # Try for a larger minimum distance
            else:
                high = mid - 1  # Try for a smaller minimum distance

        return result




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends