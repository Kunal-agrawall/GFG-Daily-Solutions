class Solution:
    def minIncrements(self, arr):
        arr.sort()  # Step 1: Sort the array
        increments = 0

        for i in range(1, len(arr)):
            # If the current element is not unique
            if arr[i] <= arr[i - 1]:
                # Calculate how much to increment to make it unique
                required_increment = arr[i - 1] + 1 - arr[i]
                arr[i] += required_increment  # Make the element unique
                increments += required_increment  # Accumulate the total increments

        return increments


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends