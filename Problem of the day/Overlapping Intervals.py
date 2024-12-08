class Solution:
    def mergeOverlap(self, arr):
        # Sort the intervals based on the starting time
        arr.sort(key=lambda x: x[0])
        
        merged = []
        for interval in arr:
            # If the list of merged intervals is empty 
            # or the current interval does not overlap with the last one, append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so merge the current and previous intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends