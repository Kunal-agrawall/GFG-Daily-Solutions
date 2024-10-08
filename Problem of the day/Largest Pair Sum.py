from typing import List

class Solution:
    def pairsum(self, arr: List[int]) -> int:
        # Initialize the two largest elements
        first, second = float('-inf'), float('-inf')
        
        # Traverse the array to find the largest and second largest
        for num in arr:
            if num > first:
                second = first  # Move current largest to second
                first = num     # Update the largest
            elif num > second:
                second = num    # Update the second largest
        
        # Return the sum of the two largest numbers
        return first + second



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

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.pairsum(arr)

        print(res)

# } Driver Code Ends