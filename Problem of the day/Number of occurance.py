class Solution:
    def countFreq(self, arr, target):
        def binary_search_first(arr, target):
            """Find the first occurrence of target using binary search."""
            left, right = 0, len(arr) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    first = mid
                    right = mid - 1  # Continue searching in the left half
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def binary_search_last(arr, target):
            """Find the last occurrence of target using binary search."""
            left, right = 0, len(arr) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    last = mid
                    left = mid + 1  # Continue searching in the right half
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        # Find the first and last occurrence of the target
        first_index = binary_search_first(arr, target)
        last_index = binary_search_last(arr, target)

        # If the target is not found, return 0
        if first_index == -1 or last_index == -1:
            return 0

        # Calculate the number of occurrences
        return last_index - first_index + 1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends