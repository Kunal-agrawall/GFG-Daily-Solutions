#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

class Solution:
    def power(self, b: float, e: int) -> float:
        # Using fast exponentiation (binary exponentiation)
        result = pow(b, e)
        
        # Clamping result to the range [-10^4, 10^4]
        return max(-10**4, min(result, 10**4))


        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends