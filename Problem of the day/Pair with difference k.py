class Solution:
    def countPairsWithDiffK(self, arr, k):
        freq = {}
        count = 0
        
        # Iterate through each element in arr
        for x in arr:
            # Check if (x + k) exists in the frequency map
            if (x + k) in freq:
                count += freq[x + k]
                
            # Check if (x - k) exists in the frequency map
            if (x - k) in freq:
                count += freq[x - k]
                
            # Add the current element to the frequency map
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        
        return count




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends