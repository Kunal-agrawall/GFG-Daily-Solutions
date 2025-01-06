class Solution:
    def sumClosest(self, arr, target):
        # Sort the array
        arr.sort()
        n = len(arr)

        # Initialize variables to track the closest sum and the best pair
        closest_sum = float('inf')
        best_pair = []

        # Two-pointer technique
        left, right = 0, n - 1

        while left < right:
            a, b = arr[left], arr[right]
            current_sum = a + b

            # Check if the current pair is better
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                best_pair = [a, b]
            elif abs(current_sum - target) == abs(closest_sum - target):
                # If sums are equally close, choose the pair with maximum absolute difference
                if abs(b - a) > abs(best_pair[1] - best_pair[0]):
                    best_pair = [a, b]

            # Move pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break  # Exact match found

        # Return the pair in sorted order
        return best_pair if best_pair else []



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends