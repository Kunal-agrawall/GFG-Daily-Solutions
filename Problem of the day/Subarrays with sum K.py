class Solution:
    def countSubarrays(self, arr, k):
        # Initialize variables
        prefix_sum_count = {0: 1}  # To handle the case where subarray starts at index 0
        current_sum = 0
        count = 0
        
        # Traverse the array
        for num in arr:
            # Update the running sum
            current_sum += num
            
            # Check if (current_sum - k) exists in the hashmap
            if current_sum - k in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            
            # Update the hashmap with the current sum
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return count


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
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends