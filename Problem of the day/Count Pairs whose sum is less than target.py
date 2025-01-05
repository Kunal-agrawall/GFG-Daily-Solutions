#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Sort the array
        arr.sort()
        
        # Initialize pointers and counter
        left = 0
        right = len(arr) - 1
        count = 0
        
        # Two-pointer approach
        while left < right:
            if arr[left] + arr[right] < target:
                # All pairs with the current left will work
                count += (right - left)
                left += 1
            else:
                # Reduce the right pointer
                right -= 1
        
        return count



    

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends