class Solution:
    def rob_linear(self, nums):
        prev2, prev1 = 0, 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2, prev1 = prev1, current
        return prev1

    def maxValue(self, arr):
        if len(arr) == 2:
            return max(arr)  # Choose the max of the two, since they are adjacent
        
        return max(self.rob_linear(arr[1:]), self.rob_linear(arr[:-1]))  # Two cases



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends