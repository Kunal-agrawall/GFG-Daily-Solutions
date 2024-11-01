class Solution:
    def maxSum(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Arrange the array in max-min alternate fashion
        n = len(arr)
        max_min_arr = []
        i, j = 0, n - 1
        while i <= j:
            if i != j:
                max_min_arr.append(arr[j])
                max_min_arr.append(arr[i])
            else:
                max_min_arr.append(arr[i])
            i += 1
            j -= 1

        # Step 3: Calculate the sum of absolute differences
        max_sum = 0
        for k in range(1, n):
            max_sum += abs(max_min_arr[k] - max_min_arr[k - 1])
        
        # Include the circular difference between the last and the first element
        max_sum += abs(max_min_arr[n - 1] - max_min_arr[0])
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends