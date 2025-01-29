
class Solution:
    def nQueen(self, n):
        def is_safe(row, col, queens):
            for prev_col, prev_row in enumerate(queens):
                if prev_row == row or abs(prev_row - row) == abs(prev_col - col):
                    return False
            return True
        
        def solve(col, queens, solutions):
            if col == n:
                solutions.append(queens[:])
                return
            
            for row in range(1, n + 1):
                if is_safe(row, col, queens):
                    queens.append(row)
                    solve(col + 1, queens, solutions)
                    queens.pop()
        
        solutions = []
        solve(0, [], solutions)
        return solutions


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends