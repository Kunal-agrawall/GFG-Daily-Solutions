class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr):
        # Helper function to merge two halves and count inversions.
        def merge_and_count(arr, temp, left, mid, right):
            i, j, k = left, mid + 1, left
            inv_count = 0

            # Merge two subarrays while counting inversions.
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)  # Count inversions
                    j += 1
                k += 1

            # Copy the remaining elements of the left subarray (if any).
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of the right subarray (if any).
            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray back to the original array.
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return inv_count

        # Recursive function to implement merge sort and count inversions.
        def merge_sort_and_count(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_and_count(arr, temp, left, mid)
                inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
                inv_count += merge_and_count(arr, temp, left, mid, right)

            return inv_count

        # Create a temporary array for merge sort.
        n = len(arr)
        temp = [0] * n
        return merge_sort_and_count(arr, temp, 0, n - 1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends