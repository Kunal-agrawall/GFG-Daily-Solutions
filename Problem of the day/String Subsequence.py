class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        MOD = 10**9 + 7
        n = len(s1)
        m = len(s2)
        
        # Create the DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # An empty s2 can be formed from any prefix of s1 by deleting all characters
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][m]


solution = Solution()



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends