class Solution:
    def countWays(self, digits: str) -> int:
        n = len(digits)
        if n == 0 or digits[0] == '0':
            return 0
        
        # DP array
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Empty string and first digit

        for i in range(2, n + 1):
            # Single digit decoding (digits[i-1] is not '0')
            if digits[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Two digit decoding (digits[i-2] and digits[i-1] form a valid number)
            two_digit = int(digits[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends