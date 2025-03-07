class Solution:
    def longestPalinSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Build the table bottom-up
        for length in range(2, n + 1):  # Substring lengths
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]  # Expand known palindrome
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # Ignore one character
        
        return dp[0][n - 1]  # The whole string's LPS length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
        print("~")
# } Driver Code Ends