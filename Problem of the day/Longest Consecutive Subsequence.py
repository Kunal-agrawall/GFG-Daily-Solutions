# User function Template for python3

class Solution:
    
    # arr[] : the input array
    
    # Function to return the length of the longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        # Convert the array into a set for O(1) lookups.
        nums_set = set(arr)
        longest_streak = 0
        
        # Iterate through each number in the array.
        for num in nums_set:
            # Check if it's the start of a sequence.
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                
                # Count the length of the sequence.
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found so far.
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends