class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        seen = set()
        
        for i in range(len(arr)):
            # Check if current element is already in the set
            if arr[i] in seen:
                return True
            
            # Add current element to the set
            seen.add(arr[i])
            
            # If the window size exceeds k, remove the element that's out of the window
            if i >= k:
                seen.remove(arr[i - k])
        
        return False
        

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if _name_ == "_main_":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends