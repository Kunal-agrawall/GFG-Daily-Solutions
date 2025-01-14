class Solution:
    # Function to find the first equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        # Iterate through the array to find the equilibrium point
        for i in range(len(arr)):
            # Calculate the right sum by subtracting current element and left sum
            right_sum = total_sum - left_sum - arr[i]

            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i  # Return the 0-based index

            # Update the left sum by adding the current element
            left_sum += arr[i]

        # If no equilibrium point found, return -1
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends