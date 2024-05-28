from typing import List

class Solution:
    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        # Initialize the dp array with "infinity" for impossible weights
        dp = [float('inf')] * (w + 1)
        dp[0] = 0  # Cost to buy 0 kg of oranges is 0
        
        # Fill the dp array
        for i in range(1, n + 1):
            if cost[i - 1] != -1:  # Only consider available packets
                for j in range(i, w + 1):
                    if dp[j - i] != float('inf'):
                        dp[j] = min(dp[j], dp[j - i] + cost[i - 1])
        
        # If dp[w] is still infinity, it's not possible to form weight w
        return dp[w] if dp[w] != float('inf') else -1


solution = Solution()


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

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends