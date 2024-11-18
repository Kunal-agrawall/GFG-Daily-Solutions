class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        # Handling cases where d >= len(arr) by using modulo
        n = len(arr)
        d %= n
        
        # Step 1: Reverse the first d elements
        self.reverse(arr, 0, d - 1)
        
        # Step 2: Reverse the remaining elements
        self.reverse(arr, d, n - 1)
        
        # Step 3: Reverse the entire array
        self.reverse(arr, 0, n - 1)
    
    # Helper function to reverse a part of the array
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends