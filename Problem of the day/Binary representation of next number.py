class Solution:
    def binaryNextNumber(self, s: str) -> str:
        # Convert the string into a list of characters for easier manipulation
        s_list = list(s)
        
        # Initialize carry as 1 because we are adding 1
        carry = 1
        n = len(s_list)
        
        # Process each bit from right to left
        for i in range(n - 1, -1, -1):
            if carry == 1:
                if s_list[i] == '1':
                    s_list[i] = '0'
                else:  # s_list[i] == '0'
                    s_list[i] = '1'
                    carry = 0
                    break  # No need to continue once carry is 0

        # If carry is still 1 after processing all bits, prepend '1'
        if carry == 1:
            s_list.insert(0, '1')
        
        # Convert the list of characters back into a string and remove leading zeros
        result = ''.join(s_list).lstrip('0')
        
        # Handle the case where the entire string was '0's and we need at least one '0'
        return result if result else '0'

# Example usage
solution = Solution()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends