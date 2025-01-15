class Solution:
    def longestSubarray(self, arr, k):
        # Dictionary to store the first occurrence of each cumulative sum
        sum_map = {}
        max_length = 0
        current_sum = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            # Check if the subarray from the beginning has the required sum
            if current_sum == k:
                max_length = i + 1

            # Check if there is a prefix sum that can be removed to get the sum k
            if (current_sum - k) in sum_map:
                max_length = max(max_length, i - sum_map[current_sum - k])

            # Store the current sum if it is not already in the map
            if current_sum not in sum_map:
                sum_map[current_sum] = i

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends