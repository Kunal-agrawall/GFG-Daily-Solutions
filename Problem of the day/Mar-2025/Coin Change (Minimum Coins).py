class Solution:
    def minCoins(self, coins, target):
        # Initialize DP array with inf (impossible values)
        dp = [float('inf')] * (target + 1)
        dp[0] = 0  # Base case: 0 coins needed for sum 0

        # Process each coin
        for coin in coins:
            for j in range(coin, target + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        # If target sum is unreachable, return -1
        return dp[target] if dp[target] != float('inf') else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends