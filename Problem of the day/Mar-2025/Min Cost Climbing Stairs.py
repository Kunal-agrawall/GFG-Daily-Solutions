class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        prev1, prev2 = 0, 0  # Represents dp[i-1] and dp[i-2]

        for i in range(2, n + 1):
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2, prev1 = prev1, current  # Shift values
        
        return prev1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends