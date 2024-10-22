class Solution:
    def sameOccurrence(self, arr, x, y):
        # Dictionary to store the occurrences of differences
        diff_map = {0: 1}  # To handle the case when there's an equal number from the start
        current_diff = 0
        count = 0
        
        for num in arr:
            if num == x:
                current_diff += 1
            elif num == y:
                current_diff -= 1
            
            # If this difference has been seen before, it means there's a subarray with equal x and y
            if current_diff in diff_map:
                count += diff_map[current_diff]
            
            # Add or update the current_diff in the hash map
            diff_map[current_diff] = diff_map.get(current_diff, 0) + 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends