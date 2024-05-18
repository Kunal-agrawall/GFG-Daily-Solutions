from collections import deque


class Solution:

    def check(self, a, mid):
        n = len(a)
        m = len(a[0])

        # Creating a boolean matrix to keep track of visited cells.
        vis = [[False] * m for _ in range(n)]

        q = deque()

        # Pushing the starting cell into the queue and marking it as visited.
        q.append((0, 0))
        vis[0][0] = True

        # Arrays to store the x and y directions for neighboring cells.
        xdir = [1, 0, -1, 0]
        ydir = [0, -1, 0, 1]

        # BFS traversal of the matrix.
        while q:
            temp = q.popleft()

            # If we reach the destination cell, return True.
            if temp[0] == n - 1 and temp[1] == m - 1:
                return True

            # Checking the neighboring cells and pushing them into the queue if valid.
            for k in range(4):
                x = temp[0] + xdir[k]
                y = temp[1] + ydir[k]

                # If the neighboring cell is out of bounds or already visited or the
                # difference in effort between the neighboring cell and the current
                # cell is greater than the mid value, skip it.
                if x < 0 or y < 0 or x >= n or y >= m or vis[x][y] or abs(
                        a[x][y] - a[temp[0]][temp[1]]) > mid:
                    continue

                # Pushing the valid neighboring cell into the queue and marking it as
                # visited.
                q.append((x, y))
                vis[x][y] = True

        return False  # If we reach here, it means we couldn't reach the destination
        # cell with the given mid value.

    def MinimumEffort(self, rows, columns, heights):
        n = len(heights)
        m = len(heights[0])

        l = 0
        h = 10**6

        # Binary search to find the minimum effort.
        while l < h:
            mid = l + (h - l) // 2

            # Checking if the mid value is feasible or not by using BFS.
            if self.check(heights, mid):
                h = mid  # If feasible, update the high value
            else:
                l = mid + 1  # If not feasible, update the low value

        return l  # Returning the minimum effort.




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

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends