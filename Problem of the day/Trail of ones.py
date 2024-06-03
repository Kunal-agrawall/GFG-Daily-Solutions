class Solution:
    def numberOfConsecutiveOnes(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 0
        
        # Base cases
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        
        # Fill the dp array
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
        # Total binary strings of length n
        total_binary_strings = pow(2, n, MOD)
        
        # Binary strings of length n without consecutive 1's
        valid_strings = dp[n]
        
        # Subtract valid strings from total to get the count of strings with consecutive 1's
        result = (total_binary_strings - valid_strings + MOD) % MOD
        
        return result

# Example usage
solution = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends