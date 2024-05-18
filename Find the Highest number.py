from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        left, right = 0, len(a) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if a[mid] < a[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return a[left]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends