class Solution:
    def max_Books(self, n, k, arr):
        max_books = 0
        current_books = 0
        left = 0
        
        for right in range(n):
            if arr[right] > k:
                # Whenever we encounter an invalid stack, we need to reset our current window
                left = right + 1
                current_books = 0
            else:
                # Expand the window
                current_books += arr[right]
                max_books = max(max_books, current_books)
        
        return max_books

# Example usage
solution = Solution()


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends