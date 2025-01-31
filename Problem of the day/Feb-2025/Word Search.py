
class Solution:
    def isWordExist(self, mat, word):
        if not mat:
            return False
        
        rows, cols = len(mat), len(mat[0])
        word_length = len(word)
        
        def dfs(r, c, index):
            if index == word_length:
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or mat[r][c] != word[index]:
                return False
            
            temp, mat[r][c] = mat[r][c], '#'  # Mark cell as visited
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            mat[r][c] = temp  # Restore cell
            return found
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends