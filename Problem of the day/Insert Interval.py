#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def insertInterval(self, intervals, newInterval):
        # Initialize result array
        merged_intervals = []
        new_start, new_end = newInterval
        i, n = 0, len(intervals)
        
        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < new_start:
            merged_intervals.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        
        # Add the merged interval
        merged_intervals.append([new_start, new_end])
        
        # Add all intervals that come after the new interval
        while i < n:
            merged_intervals.append(intervals[i])
            i += 1
        
        return merged_intervals





        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends