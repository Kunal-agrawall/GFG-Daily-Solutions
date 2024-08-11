class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n = len(arr1)
        
        if n == 0:
            return 0

        if n > len(arr2):
            arr1, arr2 = arr2, arr1  # Ensure arr1 is the smaller array
        
        low, high = 0, n
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (n + n + 1) // 2 - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else arr1[partition1 - 1]
            minRight1 = float('inf') if partition1 == n else arr1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else arr2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else arr2[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (n + n) % 2 == 0:
                    return max(maxLeft1, maxLeft2) + min(minRight1, minRight2)
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        
        raise ValueError("Input arrays are not sorted or of unequal length.")



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends