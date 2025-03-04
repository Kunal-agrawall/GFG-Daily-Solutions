class Solution:
    def lis(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        # DP array initialized to 1, since the minimum LIS is 1 for any element
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends