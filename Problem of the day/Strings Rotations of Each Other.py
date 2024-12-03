class Solution:
    
    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # Check if lengths are the same, else they cannot be rotations.
        if len(s1) != len(s2):
            return False
        
        # Concatenate s1 with itself and check if s2 is a substring of it.
        temp = s1 + s1
        return s2 in temp



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
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends