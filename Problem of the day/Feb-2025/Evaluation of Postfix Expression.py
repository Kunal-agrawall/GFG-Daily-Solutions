#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends


class Solution:
    def evaluate(self, arr):
        stack = []
        
        for token in arr:
            if token in {"+", "-", "*", "/"}:  # Check if token is an operator
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # Integer division that truncates towards zero
            else:
                stack.append(int(token))  # Convert operand to integer and push onto stack
        
        return stack[0]  # Final result is the only element left in stack




#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends