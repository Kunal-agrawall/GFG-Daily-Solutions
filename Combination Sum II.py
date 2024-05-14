class Solution:
    def CombinationSum2(self, arr, n, k):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, n):
                if i > start and arr[i] == arr[i - 1]:
                    continue
                backtrack(i + 1, target - arr[i], path + [arr[i]])

        arr.sort()
        result = []
        backtrack(0, k, [])
        return result

# Example usage
solution = Solution()
n = 5
k = 7
arr = [1, 2, 3, 3, 5]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends