class Solution:
    # Function to find the maximum product subarray
    def maxProduct(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Initialize variables
        max_ending_here = arr[0]
        min_ending_here = arr[0]
        max_so_far = arr[0]

        for i in range(1, n):
            # If the current element is negative, swap the max and min
            if arr[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here

            # Update max and min ending here
            max_ending_here = max(arr[i], max_ending_here * arr[i])
            min_ending_here = min(arr[i], min_ending_here * arr[i])

            # Update the overall maximum product
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends