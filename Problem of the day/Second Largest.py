class Solution:
    def print2largest(self, arr, n):
        # Initialize the largest and second largest with the smallest possible values
        first = second = -1
        
        # Traverse the array to find the largest and second largest distinct elements
        for value in arr:
            if value > first:
                second = first
                first = value
            elif value > second and value != first:
                second = value
        
        # If the second largest is still -1, that means there was no second distinct largest element
        return second if second != -1 else -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends