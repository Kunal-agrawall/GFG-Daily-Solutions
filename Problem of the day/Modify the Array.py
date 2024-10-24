#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)
        
        # Step 1: Modify the array by combining adjacent equal non-zero numbers
        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
        
        # Step 2: Move all non-zero numbers to the front and zeroes to the back
        # We can do this by creating a new array and filling it accordingly
        non_zero = []
        
        # Collect non-zero elements
        for num in arr:
            if num != 0:
                non_zero.append(num)
        
        # Calculate how many zeroes should be at the end
        num_zeros = n - len(non_zero)
        
        # Step 3: Replace the original array
        for i in range(len(non_zero)):
            arr[i] = non_zero[i]
        
        for i in range(len(non_zero), n):
            arr[i] = 0
        
        return arr





#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends