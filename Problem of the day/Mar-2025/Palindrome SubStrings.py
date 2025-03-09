class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0

        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:  # Count only if length is ≥ 2
                    count += 1
                left -= 1
                right += 1

        for i in range(n):
            expandAroundCenter(i, i)      # Odd-length palindromes
            expandAroundCenter(i, i + 1)  # Even-length palindromes

        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends