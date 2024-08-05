class Solution:
    def isValid(self, str):
        # Split the string by dots
        parts = str.split('.')
        
        # Check if we have exactly four parts
        if len(parts) != 4:
            return False
        
        for part in parts:
            # Check if the part is a number and within the range 0 to 255
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
            # Check for leading zeros
            if len(part) > 1 and part[0] == '0':
                return False
        
        return True




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends