class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place each positive integer x such that 1 <= x <= n at index x-1.
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        # Step 2: Find the first index where the value is not index + 1.
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # If all indices match, the missing number is n+1.
        return n + 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends