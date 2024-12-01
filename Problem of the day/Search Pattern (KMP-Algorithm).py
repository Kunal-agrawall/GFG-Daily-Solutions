class Solution:
    def search(self, pat, txt):
        # Build the LPS (Longest Prefix Suffix) array
        def computeLPSArray(pattern):
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

        # Search for the pattern using the LPS array
        def KMPSearch(text, pattern):
            n, m = len(text), len(pattern)
            lps = computeLPSArray(pattern)
            i = j = 0  # i -> index for text, j -> index for pattern
            indices = []

            while i < n:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1

                if j == m:
                    # Match found
                    indices.append(i - j)
                    j = lps[j - 1]

                elif i < n and pattern[j] != text[i]:
                    # Mismatch after j matches
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return indices

        # Edge case: If pattern is larger than the text
        if len(pat) > len(txt):
            return []

        return KMPSearch(txt, pat)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends