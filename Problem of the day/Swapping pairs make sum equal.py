class Solution:
    def findSwapValues(self, a, n, b, m):
        sumA = sum(a)
        sumB = sum(b)
        
        # If the difference is not even, we cannot split the sum equally by swapping any elements.
        if (sumA - sumB) % 2 != 0:
            return -1
        
        # Target difference we need to match with some pair (a[i] - b[j])
        target = (sumA - sumB) // 2
        
        # Sort both arrays
        a.sort()
        b.sort()
        
        # Use two pointers to find the target pair
        i, j = 0, 0
        while i < n and j < m:
            diff = a[i] - b[j]
            if diff == target:
                return 1
            elif diff < target:
                i += 1
            else:
                j += 1
        
        return -1



#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends