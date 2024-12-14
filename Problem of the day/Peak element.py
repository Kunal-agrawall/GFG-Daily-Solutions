class Solution:
    def peakElement(self, arr):
        n = len(arr)

        # Helper function for binary search
        def binary_search(left, right):
            if left == right:
                return left

            mid = (left + right) // 2

            # Check if mid is a peak
            if arr[mid] > arr[mid + 1]:
                # Potential peak on the left side (or mid itself)
                return binary_search(left, mid)
            else:
                # Potential peak on the right side
                return binary_search(mid + 1, right)

        # Edge case: If array has only one element
        if n == 1:
            return 0

        # Perform binary search
        return binary_search(0, n - 1)


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends