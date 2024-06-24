class Solution:
    def sumMatrix(self, n, q):
        lower_bound = max(1, q - n)
        upper_bound = min(n, q - 1)
        
        if lower_bound <= upper_bound:
            return upper_bound - lower_bound + 1
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
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends