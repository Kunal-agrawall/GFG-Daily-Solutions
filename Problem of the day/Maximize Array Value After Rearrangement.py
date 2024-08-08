class Solution:
    def Maximize(self, arr): 
        MOD = 10**9 + 7
        
        # Sort the array
        arr.sort()
        
        # Initialize the sum
        max_sum = 0
        
        # Calculate the sum of arr[i] * i
        for i in range(len(arr)):
            max_sum = (max_sum + arr[i] * i) % MOD
        
        return max_sum




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends