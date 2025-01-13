class Solution:
    def maxWater(self, arr):
        # Initialize two pointers and the maximum water storage
        left = 0
        right = len(arr) - 1
        max_water = 0

        # Two-pointer approach to find the maximum container area
        while left < right:
            # Calculate width and height for the container formed by arr[left] and arr[right]
            width = right - left
            height = min(arr[left], arr[right])
            current_water = width * height

            # Update max_water if current container holds more water
            max_water = max(max_water, current_water)

            # Move the pointer pointing to the shorter line inward
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_water

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends