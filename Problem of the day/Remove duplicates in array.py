#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def removeDuplicates(self, arr):
        # Use a set to track seen elements and preserve order in the result list
        seen = set()
        result = []
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if _name_ == "_main_":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends