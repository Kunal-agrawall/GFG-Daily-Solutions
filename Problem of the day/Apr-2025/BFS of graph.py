from collections import deque

class Solution:
    def bfs(self, adj):
        visited = set()  # To track visited nodes
        queue = deque([0])  # BFS Queue starting from node 0
        visited.add(0)  
        bfs_order = []  # Result list
        
        while queue:
            node = queue.popleft()  # Pop the front node
            bfs_order.append(node)
            
            # Explore neighbors in the given order
            for neighbor in adj[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        return bfs_order


#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends