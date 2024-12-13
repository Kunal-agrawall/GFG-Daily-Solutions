class Solution:
    def findMin(self, arr):
        # Initialize pointers
        low, high = 0, len(arr) - 1

        # If the array is not rotated (or only one element exists)
        if arr[low] <= arr[high]:
            return arr[low]

        # Binary search to find the minimum element
        while low <= high:
            mid = (low + high) // 2

            # Check if mid is the minimum element
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return arr[mid]

            # Check if mid + 1 is the minimum element
            if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]

            # Decide the search space
            if arr[mid] >= arr[low]:
                # Minimum element lies in the right half
                low = mid + 1
            else:
                # Minimum element lies in the left half
                high = mid - 1

        return -1  # This should not happen in a valid rotated sorted array


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends