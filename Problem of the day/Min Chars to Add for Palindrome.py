class Solution:
    def minChar(self, s):
        # Combine the original string and its reverse with a separator
        temp = s + "#" + s[::-1]
        
        # Compute the LPS (Longest Prefix Suffix) array for the combined string
        n = len(temp)
        lps = [0] * n
        j = 0  # Length of the previous longest prefix suffix

        for i in range(1, n):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
                lps[i] = j

        # The length of the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]

        # Characters to add at the front
        return len(s) - longest_palindromic_prefix_length



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends