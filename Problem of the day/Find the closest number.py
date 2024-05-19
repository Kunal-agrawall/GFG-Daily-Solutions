from typing import List

class Solution:
    def findClosest(self, n: int, k: int, arr: List[int]) -> int:
        left, right = 0, n - 1
        
        # Binary search to find the closest position
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == k:
                return arr[mid]
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # Post-processing to find the closest value
        # left is the smallest element greater than k (or out of bounds)
        # right is the largest element less than k (or out of bounds)
        
        if left >= n:
            return arr[right]
        if right < 0:
            return arr[left]
        
        # Compare the differences
        if abs(arr[left] - k) < abs(arr[right] - k):
            return arr[left]
        elif abs(arr[left] - k) > abs(arr[right] - k):
            return arr[right]
        else:
            # If both differences are equal, return the greater value
            return max(arr[left], arr[right])




#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends