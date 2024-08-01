class Solution:
    def editDistance(self, str1, str2):
        m = len(str1)
        n = len(str2)
        
        # Initialize DP table
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Base cases: converting str1 to empty string (all deletions)
        for i in range(m + 1):
            dp[i][0] = i
        
        # Base cases: converting empty string to str2 (all insertions)
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,    # Delete
                                   dp[i][j - 1] + 1,    # Insert
                                   dp[i - 1][j - 1] + 1) # Replace
        
        # The result is in the bottom-right cell of the table
        return dp[m][n]

# Example usage:
sol = Solution()


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends