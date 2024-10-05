class Solution:
    def findSmallest(self, arr):
        # Sort the array first (greedy approach works only on sorted arrays)
        arr.sort()
        
        # Initialize the smallest missing value to 1
        smallest_missing = 1
        
        # Traverse through all elements in the sorted array
        for num in arr:
            # If current number is greater than the smallest missing, return it
            if num > smallest_missing:
                return smallest_missing
            
            # Otherwise, add the current number to smallest_missing
            smallest_missing += num
        
        # If all numbers were processed, return the final smallest missing value
        return smallest_missing


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends