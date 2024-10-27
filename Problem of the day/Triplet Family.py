class Solution:
    def findTriplet(self, arr):
        # Sort the array to use the two-pointer technique
        arr.sort()
        n = len(arr)
        
        # Traverse each element considering it as the target sum (arr[i] as "c")
        for i in range(2, n):
            target = arr[i]
            left, right = 0, i - 1
            
            # Use two pointers to find if there's a pair summing to target
            while left < right:
                current_sum = arr[left] + arr[right]
                
                if current_sum == target:
                    return True  # Triplet found
                
                elif current_sum < target:
                    left += 1  # Increase the sum by moving the left pointer right
                
                else:
                    right -= 1  # Decrease the sum by moving the right pointer left
        
        return False  # No triplet found


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends