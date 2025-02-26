class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        
        # Step 1: Compute previous and next smaller elements
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        stack = []
        
        # Finding previous smaller element index for each element
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        stack = []
        
        # Finding next smaller element index for each element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
        
        # Step 2: Compute result for each possible window size
        result = [0] * (n + 1)
        
        for i in range(n):
            window_size = next_smaller[i] - prev_smaller[i] - 1
            result[window_size] = max(result[window_size], arr[i])
        
        # Step 3: Fill missing values (propagate max values)
        for i in range(n - 1, 0, -1):
            result[i] = max(result[i], result[i + 1])
        
        return result[1:]  # Discarding index 0 as window sizes start from 1





#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends