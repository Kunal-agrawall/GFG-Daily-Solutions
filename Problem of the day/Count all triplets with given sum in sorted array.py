class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == target:
                    # Handle duplicates for `left` and `right`
                    if arr[left] == arr[right]:
                        # All pairs between left and right are valid
                        count += (right - left + 1) * (right - left) // 2
                        break
                    else:
                        # Count occurrences of arr[left] and arr[right]
                        left_count = 1
                        right_count = 1
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            left += 1
                            left_count += 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            right -= 1
                            right_count += 1
                        count += left_count * right_count
                        left += 1
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return count



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends