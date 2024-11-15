class Solution:
    def pushZerosToEnd(self, arr):
        # Two-pointer approach
        n = len(arr)
        non_zero_index = 0  # Pointer to place the next non-zero element

        for i in range(n):
            if arr[i] != 0:
                # Swap the non-zero element with the element at non_zero_index
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends