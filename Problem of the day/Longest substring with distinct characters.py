
class Solution:
    def longestUniqueSubstr(self, s):
        # Dictionary to store the last position of each character
        last_seen = {}
        
        # Initialize pointers for the sliding window and the max length
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            # If the character is already in the dictionary and within the window
            if s[end] in last_seen and last_seen[s[end]] >= start:
                # Move the start to one position right of the last occurrence
                start = last_seen[s[end]] + 1
            
            # Update the last seen position of the character
            last_seen[s[end]] = end
            
            # Update the maximum length found so far
            max_length = max(max_length, end - start + 1)
        
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends