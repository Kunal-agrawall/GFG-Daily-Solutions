class Solution:
    def addBinary(self, s1, s2):
        # Convert binary strings to integers
        num1 = int(s1, 2)
        num2 = int(s2, 2)
        
        # Perform addition
        result = num1 + num2
        
        # Convert the result back to a binary string and strip the "0b" prefix
        binary_result = bin(result)[2:]
        
        return binary_result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends