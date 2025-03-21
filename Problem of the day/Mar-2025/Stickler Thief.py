class Solution:
    def findMaxSum(self, arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]

        prev2, prev1 = 0, arr[0]  # Initialize base cases

        for i in range(1, len(arr)):
            current = max(prev1, arr[i] + prev2)  # Max of (skip or loot)
            prev2, prev1 = prev1, current  # Shift variables for next iteration

        return prev1


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends