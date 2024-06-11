from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Create a list of tuples where each tuple is (tip difference, tip if A takes, tip if B takes)
        differences = [(abs(arr[i] - brr[i]), arr[i], brr[i]) for i in range(n)]
        
        # Sort the differences list based on the absolute difference in descending order
        differences.sort(reverse=True, key=lambda x: x[0])
        
        total_tips = 0
        count_a = 0
        count_b = 0
        
        for diff, tip_a, tip_b in differences:
            if (tip_a >= tip_b and count_a < x) or count_b >= y:
                total_tips += tip_a
                count_a += 1
            else:
                total_tips += tip_b
                count_b += 1
        
        return total_tips

# Example usage:
solution = Solution()
n = 5
x = 3
y = 3
arr = [8, 7, 15, 19, 10]
brr = [1, 2, 5, 8, 9]
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends