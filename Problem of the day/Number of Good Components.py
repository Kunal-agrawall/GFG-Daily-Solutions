import collections
from collections import deque  #importing deque from collections module
from collections import defaultdict  #importing defaultdict from collections module


class Solution:

    #Depth First Search algorithm to traverse the graph
    def dfs(self, v, adj, visited):
        visited[v] = 1  #marking the current vertex as visited
        self.vertices += 1  #incrementing the vertex count
        self.edges += len(
            adj[v]
        )  #adding the number of edges connected to the current vertex

        #iterating over all the adjacent vertices
        for to in adj[v]:
            if not visited[to]:  #if the adjacent vertex is not visited
                self.dfs(to, adj, visited)  #recursive call to dfs function

    #Function to find the number of good components
    def findNumberOfGoodComponent(self, E, V, edges):
        ans = 0  #variable to store the count of good components
        visited = [0] * (V + 1)  #array to mark visited vertices
        adj = [[] for _ in range(V + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(1, V + 1):
            if not visited[i]:  #if the vertex is not visited
                self.vertices = 0  #initialize vertex count to 0
                self.edges = 0  #initialize edge count to 0
                self.dfs(
                    i, adj, visited
                )  #call to dfs function to traverse the graph starting from current vertex

                self.edges //= 2  #divide the edge count by 2 as each edge is counted twice
                if (
                        self.edges == (self.vertices *
                                       (self.vertices - 1)) // 2
                ):  #check if the number of edges is equal to the number of vertices choose 2
                    ans += 1  #increment the count of good components

        return ans  #return the count of good components


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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        e = int(input())

        v = int(input())

        edges = IntMatrix().Input(e, 2)

        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)

        print(res)

# } Driver Code Ends