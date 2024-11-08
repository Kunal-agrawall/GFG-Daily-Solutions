class Solution:
    def minSum(self, arr):
        # Edge case: if the array is empty or contains only zeros
        if not arr:
            return "0"
        
        # Sort the digits in ascending order
        arr.sort()
        
        # Two strings to store the two numbers
        num1 = ""
        num2 = ""
        
        # Alternate between the two numbers to minimize their values
        for i in range(len(arr)):
            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
        
        # Function to perform string-based addition to avoid large integer limits
        def add_strings(num1, num2):
            i, j = len(num1) - 1, len(num2) - 1
            carry = 0
            result = []
            
            # Add digits from the end of both strings
            while i >= 0 or j >= 0 or carry:
                digit1 = int(num1[i]) if i >= 0 else 0
                digit2 = int(num2[j]) if j >= 0 else 0
                total = digit1 + digit2 + carry
                carry = total // 10
                result.append(str(total % 10))
                i -= 1
                j -= 1
            
            # The result is in reverse order, so reverse it back
            return ''.join(result[::-1])
        
        # Get the sum as a string without leading zeros
        result = add_strings(num1, num2).lstrip("0")
        return result if result else "0"



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends