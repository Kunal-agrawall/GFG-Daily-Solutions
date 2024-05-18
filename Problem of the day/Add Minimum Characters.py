class Solution:
    def addMinChar(self, str1):
        def computeLPS(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Creating the combined string
        combined = str1 + "#" + str1[::-1]
        lps = computeLPS(combined)
        
        # Length of the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]
        
        # Minimum characters to add
        min_chars_to_add = len(str1) - longest_palindromic_prefix_length
        
        return min_chars_to_add




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends