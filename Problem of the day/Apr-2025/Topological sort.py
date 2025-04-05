from collections import deque, defaultdict

class Solution:
    
    def topoSort(self, V, edges):
        # Step 1: Build adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Step 2: Queue all vertices with in-degree 0
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        topo_order = []

        # Step 3: Process the queue
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if topological sort is possible
        if len(topo_order) == V:
            return topo_order
        else:
            return []  # cycle detected, not a DAG




#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, V, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends