#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def calculateSpan(self, prices):
        n = len(prices)
        span = [1] * n  # Initialize span array with 1
        stack = []  # Stack to store indices
        
        for i in range(n):
            # Pop elements from stack while stack is not empty and stack top is smaller than current price
            while stack and prices[stack[-1]] <= prices[i]:
                stack.pop()
            
            # If stack is empty, price[i] is the highest so far, span is i+1
            if not stack:
                span[i] = i + 1
            else:
                # Difference between current index and last higher price index
                span[i] = i - stack[-1]
            
            # Push this element's index onto stack
            stack.append(i)
        
        return span



        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends