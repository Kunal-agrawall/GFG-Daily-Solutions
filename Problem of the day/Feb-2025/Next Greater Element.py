class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n  # Initialize result array with -1
        stack = []  # Stack to keep track of elements for comparison

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # Pop elements from the stack while they are smaller than or equal to arr[i]
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            # If stack is not empty, the top element is the next greater element
            if stack:
                result[i] = stack[-1]

            # Push current element onto the stack
            stack.append(arr[i])

        return result


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends