class Solution:
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, k, arr):
        # This will store the result
        result = []
        
        # Create a deque to store indices of array elements
        dq = deque()
        
        # Iterate through each element in the array
        for i in range(len(arr)):
            # Remove indices that are out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # Remove all elements that are smaller than the current element
            # from the deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # Add current element index to the deque
            dq.append(i)
            
            # Start adding results to the list once we have processed the first 'k' elements
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(k, arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends