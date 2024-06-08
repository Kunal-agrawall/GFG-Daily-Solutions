class Solution:
    def findExtra(self, n, a, b):
        # Binary search for the index of the extra element
        low, high = 0, n - 2  # arr2 has n-1 elements, so we start high at n-2

        while low <= high:
            mid = (low + high) // 2

            if a[mid] == b[mid]:
                # Extra element is in the right half
                low = mid + 1
            else:
                # Extra element is in the left half or is at mid
                high = mid - 1

        # After the loop, low is the index of the extra element
        return low




#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends