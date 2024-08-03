class Solution:
    def celebrity(self, mat):
        n = len(mat)
        # Step 1: Find a potential candidate
        candidate = 0
        for i in range(1, n):
            if mat[candidate][i] == 1:
                candidate = i

        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate

# Example usage:
sol = Solution()
mat = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]



#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends