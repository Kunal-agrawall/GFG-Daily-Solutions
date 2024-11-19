class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:  # If a valid decreasing element was found
            # Step 2: Find the next larger element to swap with
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            # Step 3: Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the elements from i+1 to the end to make them the smallest possible order
        arr[i + 1:] = reversed(arr[i + 1:])
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends