class Solution:
    def myAtoi(self, s):
        # Initialize variables
        i, n = 0, len(s)
        result = 0
        sign = 1  # Default to positive
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check for a sign ('+' or '-')
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read the integer
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')  # Convert character to integer
            result = result * 10 + digit
            i += 1
        
        # Apply sign
        result *= sign
        
        # Step 4: Clamp the result to the 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends