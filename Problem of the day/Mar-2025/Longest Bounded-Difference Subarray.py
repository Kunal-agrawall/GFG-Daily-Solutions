from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        left = 0  # Left pointer of the sliding window
        max_dq = deque()  # Monotonic decreasing deque to track max values
        min_dq = deque()  # Monotonic increasing deque to track min values
        max_length = 0  # Store the max length of the valid subarray
        start_index = 0  # Store the start index of the longest valid subarray
        
        for right in range(len(arr)):
            # Maintain max deque
            while max_dq and arr[max_dq[-1]] < arr[right]:
                max_dq.pop()
            max_dq.append(right)
            
            # Maintain min deque
            while min_dq and arr[min_dq[-1]] > arr[right]:
                min_dq.pop()
            min_dq.append(right)
            
            # If the window becomes invalid, shrink it from the left
            while arr[max_dq[0]] - arr[min_dq[0]] > x:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
            
            # Update max_length and start_index if we find a longer valid subarray
            if right - left + 1 > max_length:
                max_length = right - left + 1
                start_index = left
        
        return arr[start_index:start_index + max_length]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends