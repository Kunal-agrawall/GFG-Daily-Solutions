class Solution:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to track the minimum elements

    def push(self, x):
        self.stack.append(x)
        # Push to min_stack only if it's empty or x is smaller/equal to current min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            # If the popped element is the minimum, remove it from min_stack as well
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else -1

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1


#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends