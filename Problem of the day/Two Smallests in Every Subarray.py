class Solution:
    def pairWithMaxSum(self, arr):
        # If there are less than 2 elements, return -1 (no subarray possible)
        if len(arr) < 2:
            return -1
        
        # Initialize the max_sum with a very small value
        max_sum = float('-inf')
        
        # Iterate through the array and calculate the sum of each adjacent pair
        for i in range(len(arr) - 1):
            # Calculate the sum of the current pair
            curr_sum = arr[i] + arr[i + 1]
            # Update max_sum if the current pair's sum is greater
            max_sum = max(max_sum, curr_sum)
        
        return max_sum


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends