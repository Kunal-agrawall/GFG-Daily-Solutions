class Solution:
    
    # Function to check whether two strings are anagrams of each other or not.
    def areAnagrams(self, s1, s2):
        # If the lengths of the strings are not equal, they cannot be anagrams
        if len(s1) != len(s2):
            return False
        
        # Using a dictionary to count occurrences of each character in both strings
        char_count = {}

        # Count characters in the first string
        for char in s1:
            char_count[char] = char_count.get(char, 0) + 1

        # Subtract counts for characters in the second string
        for char in s2:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        # Check if all counts are zero
        for count in char_count.values():
            if count != 0:
                return False

        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends