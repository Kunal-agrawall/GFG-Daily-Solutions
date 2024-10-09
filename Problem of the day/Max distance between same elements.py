class Solution:
    # Function should return an integer
    def maxDistance(self, arr):
        # Dictionary to store the first occurrence of each element
        first_occurrence = {}
        max_dist = 0

        # Traverse through the array
        for i in range(len(arr)):
            # If element is seen for the first time, store its index
            if arr[i] not in first_occurrence:
                first_occurrence[arr[i]] = i
            else:
                # If element is seen before, calculate the distance
                dist = i - first_occurrence[arr[i]]
                # Update the max distance
                max_dist = max(max_dist, dist)
        
        return max_dist



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends