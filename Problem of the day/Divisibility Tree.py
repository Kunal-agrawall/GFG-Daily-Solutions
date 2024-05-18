class Solution:
    def minimumEdgeRemove(self, n, edges):
        from collections import defaultdict
        
        # Create an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # To store subtree sizes
        subtree_sizes = [0] * (n + 1)
        # To keep track of visited nodes
        visited = [False] * (n + 1)
        # This will hold our count of minimum edge removals
        cuts = 0
        
        # DFS function to compute subtree sizes
        def dfs(node):
            nonlocal cuts
            visited[node] = True
            subtree_size = 1  # Count the current node
            
            # Traverse all adjacent nodes
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    subtree_size += dfs(neighbor)
            
            subtree_sizes[node] = subtree_size
            
            # If the subtree size is even, we can cut the edge to its parent
            if subtree_size % 2 == 0:
                cuts += 1
            
            return subtree_size
        
        # Start DFS from the root (assuming the root is node 1)
        dfs(1)
        
        # The root node's subtree size is the whole tree which is n
        # We do not consider cutting the entire tree, so we subtract 1 if it's even
        if subtree_sizes[1] % 2 == 0:
            cuts -= 1
        
        return cuts

# Example usage
sol = Solution()
n = 10
edges = [[2, 1], [3, 1], [4, 3], [5, 2], [6, 1], [7, 2], [8, 6], [9, 8], [10, 8]]





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

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends