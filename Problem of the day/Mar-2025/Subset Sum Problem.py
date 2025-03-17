class Solution:
    def isSubsetSum(self, arr, sum):
        n = len(arr)
        dp = [False] * (sum + 1)
        dp[0] = True  # Sum 0 is always achievable

        for num in arr:
            for j in range(sum, num - 1, -1):  # Traverse from back to avoid overwriting
                dp[j] = dp[j] or dp[j - num]

        return dp[sum]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends