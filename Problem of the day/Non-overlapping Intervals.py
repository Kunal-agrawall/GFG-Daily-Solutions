#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def minRemoval(self, intervals):
        # Sort intervals by their ending time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        end = float('-inf')  # End time of the last interval in the non-overlapping set
        removals = 0
        
        for start, finish in intervals:
            # Check for overlap
            if start < end:
                removals += 1  # Remove the current interval
            else:
                end = finish  # Update the end time to the current interval's end
        
        return removals





#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends