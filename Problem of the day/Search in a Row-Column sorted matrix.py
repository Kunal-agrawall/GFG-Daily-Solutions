class Solution:
    def matSearch(self, mat, x):
        n = len(mat)    # Number of rows
        m = len(mat[0]) # Number of columns
        
        # Start from the top-right corner
        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1  # Move left
            else:
                row += 1  # Move down
        
        return False  # Element not found


#{ 
 # Driver Code Starts
# Initial Template for Python 3

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
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.matSearch(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends