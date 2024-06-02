from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        s = [0]  # Initial list with a single value 0
        cumulative_xor = 0  # To store cumulative XOR value
        
        for query in queries:
            if query[0] == 0:
                # Insert the value x into the list adjusted by cumulative XOR
                s.append(query[1] ^ cumulative_xor)
            elif query[0] == 1:
                # Update the cumulative XOR value
                cumulative_xor ^= query[1]
        
        # Apply cumulative XOR to all elements in the list before sorting
        s = [a ^ cumulative_xor for a in s]
        
        # Sort the final list
        s.sort()
        
        return s

# Example usage
solution = Solution()




#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


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

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)

# } Driver Code Ends