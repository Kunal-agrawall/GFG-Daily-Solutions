class Solution:
    ## Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_sum = float('-inf')  # To handle negative arrays
        current_sum = 0
        
        for num in arr:
            # Add current element to current_sum or start a new subarray
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends