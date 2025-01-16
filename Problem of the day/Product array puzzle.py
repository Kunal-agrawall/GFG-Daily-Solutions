
class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)

        # Initialize the result array with 1
        res = [1] * n

        # Compute the prefix product for each element
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]

        # Compute the suffix product for each element
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]

        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends