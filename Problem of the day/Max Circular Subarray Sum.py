def circularSubarraySum(arr):
    # Function to find the maximum subarray sum using Kadane's Algorithm
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Find the maximum subarray sum (non-circular case)
    max_kadane = kadane(arr)

    # Calculate the total sum of the array
    total_sum = sum(arr)

    # Find the minimum subarray sum
    # Negate the elements and apply Kadane's Algorithm
    min_kadane = kadane([-x for x in arr])

    # Maximum circular subarray sum is total_sum - (-min_kadane)
    max_circular = total_sum + min_kadane

    # Handle case when all elements are negative
    # If max_circular is 0, it means the entire array is negated.
    if max_circular == 0:
        return max_kadane

    # Return the maximum of the two cases
    return max(max_kadane, max_circular)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends