#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        result = []
        i, j = 0, 0
        
        # Traverse both arrays
        while i < len(a) and j < len(b):
            # If we encounter duplicate elements in result, skip them
            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
            if j > 0 and b[j] == b[j - 1]:
                j += 1
                continue
            
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif b[j] < a[i]:
                result.append(b[j])
                j += 1
            else:
                # Both are equal
                result.append(a[i])
                i += 1
                j += 1
        
        # Collect remaining elements of a[]
        while i < len(a):
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1
        
        # Collect remaining elements of b[]
        while j < len(b):
            if j == 0 or b[j] != b[j - 1]:
                result.append(b[j])
            j += 1
        
        return result
        

        

#{ 
 # Driver Code Starts.
if _name_ == '_main_':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends