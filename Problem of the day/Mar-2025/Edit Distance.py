class Solution:
    def editDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j  # Insert all characters of s2
                elif j == 0:
                    dp[i][j] = i  # Remove all characters of s1
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No change needed
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],   # Insert
                                       dp[i - 1][j],   # Remove
                                       dp[i - 1][j - 1])  # Replace
        
        return dp[m][n]





#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends