class Solution:
    def padovanSequence(self, n):
        MOD = 10**9 + 7

        if n == 0 or n == 1 or n == 2:
            return 1

        p0, p1, p2 = 1, 1, 1

        for i in range(3, n + 1):
            p_next = (p0 + p1) % MOD
            p0, p1, p2 = p1, p2, p_next

        return p2

# Example usage:
solution = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends