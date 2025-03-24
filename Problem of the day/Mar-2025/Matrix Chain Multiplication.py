class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]  # Initialize DP table

        # L is the length of the sub-chain (from 2 to n-1)
        for L in range(2, n):
            for i in range(1, n - L + 1):  # Start index
                j = i + L - 1  # End index
                dp[i][j] = float('inf')  # Set to infinity initially

                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n-1]
      


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends