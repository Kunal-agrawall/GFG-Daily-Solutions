class Solution:
    def kPalindrome(self, str, n, k):
        def longest_palindromic_subsequence(s):
            rev_s = s[::-1]
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if s[i - 1] == rev_s[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
            return dp[n][n]
        
        lps_length = longest_palindromic_subsequence(str)
        if lps_length >= n - k:
            return 1
        else:
            return 0

# Example usage:
solution = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        n = int(arr[0])
        k = int(arr[1])
        str = input()

        ob = Solution()
        print(ob.kPalindrome(str, n, k))

# } Driver Code Ends