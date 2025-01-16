class Solution:
    def maxLen(self, arr):
        # Replace 0s with -1s to use the prefix sum technique
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1

        prefix_sum = 0
        max_length = 0
        prefix_map = {}  # Map to store the first occurrence of each prefix sum

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                # If the prefix sum is zero, the subarray from the start has equal 0s and 1s
                max_length = i + 1

            # If the prefix sum has been seen before, calculate the subarray length
            if prefix_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum])
            else:
                # Store the first occurrence of this prefix sum
                prefix_map[prefix_sum] = i

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends