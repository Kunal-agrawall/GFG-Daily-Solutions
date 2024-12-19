class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:  # Check for empty matrix
            return []

        n, m = len(mat), len(mat[0])  # Dimensions of the matrix
        top, bottom, left, right = 0, n - 1, 0, m - 1  # Define boundaries
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1  # Move the right boundary left

            if top <= bottom:  # Ensure there are rows remaining
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1  # Move the bottom boundary up

            if left <= right:  # Ensure there are columns remaining
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1  # Move the left boundary right

        return result



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends