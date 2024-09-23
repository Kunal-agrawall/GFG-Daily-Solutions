from collections import defaultdict

class Solution:
    
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
        
        # Dictionary to count occurrences of characters in p
        need_map = defaultdict(int)
        for char in p:
            need_map[char] += 1
        
        # Dictionary to track the current window character frequencies
        window_map = defaultdict(int)
        
        # Variables to track the smallest window
        left = 0
        min_len = float('inf')
        start_idx = 0
        have = 0  # To track how many characters are satisfying the need condition
        need = len(need_map)  # Number of distinct characters needed
        
        for right in range(len(s)):
            char = s[right]
            window_map[char] += 1
            
            # Check if the current character satisfies the requirement
            if char in need_map and window_map[char] == need_map[char]:
                have += 1
            
            # Now try to shrink the window from the left
            while have == need:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    start_idx = left
                
                # Remove the left character from window_map
                left_char = s[left]
                window_map[left_char] -= 1
                
                # Check if the removal of this character makes the window invalid
                if left_char in need_map and window_map[left_char] < need_map[left_char]:
                    have -= 1
                
                # Move the left pointer
                left += 1
        
        # If min_len was updated, return the smallest window
        if min_len == float('inf'):
            return "-1"
        else:
            return s[start_idx:start_idx + min_len]



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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends