class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # Combine start and end times into a list of tuples
        meetings = list(zip(start, end))
        
        # Sort the meetings based on their end time
        meetings.sort(key=lambda x: x[1])
        
        # Initialize variables
        count = 0
        last_end_time = 0
        
        # Iterate through sorted meetings
        for meeting in meetings:
            meeting_start, meeting_end = meeting
            if meeting_start > last_end_time:
                # If the meeting can be accommodated
                count += 1
                last_end_time = meeting_end
        
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends