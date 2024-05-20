class Solution:
    def PowMod(self, x, n, m):
        result = 1
        x = x % m  # Update x to be within the range of modulo m

        while n > 0:
            # If n is odd, multiply x with the result and take modulo m
            if n % 2 == 1:
                result = (result * x) % m
            
            # Square x and reduce n by half
            x = (x * x) % m
            n = n // 2
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends