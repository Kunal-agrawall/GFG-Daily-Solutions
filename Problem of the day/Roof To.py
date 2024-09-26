class Solution:
    
    # Function to find the maximum number of consecutive steps
    # to gain an increase in altitude with each step.
    def maxStep(self, arr):
        n = len(arr)
        max_steps = 0
        current_steps = 0
        
        # Traverse the array from the 1st to the last building.
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                current_steps += 1  # We can step forward.
            else:
                max_steps = max(max_steps, current_steps)
                current_steps = 0  # Reset current step count.
        
        # Handle the case where the last step sequence is the longest.
        max_steps = max(max_steps, current_steps)
        
        return max_steps



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends