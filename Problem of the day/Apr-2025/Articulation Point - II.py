class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        # Step 1: Create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize tracking arrays
        disc = [-1] * V  # discovery time of vertices
        low = [-1] * V   # earliest visited vertex reachable
        parent = [-1] * V
        visited = [False] * V
        ap = set()       # stores articulation points
        time = [0]       # time counter wrapped in list to mutate inside DFS

        def dfs(u):
            children = 0
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)

                    # Update low value
                    low[u] = min(low[u], low[v])

                    # Case 1: u is root and has 2+ children
                    if parent[u] == -1 and children > 1:
                        ap.add(u)

                    # Case 2: u is not root and low[v] >= disc[u]
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap.add(u)

                elif v != parent[u]:  # back edge
                    low[u] = min(low[u], disc[v])

        # In case the graph is disconnected
        for i in range(V):
            if not visited[i]:
                dfs(i)

        return sorted(ap) if ap else [-1]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends