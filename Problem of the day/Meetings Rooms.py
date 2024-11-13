class Solution:
    def canAttend(self, arr):
        # Step 1: Sort the meetings by start time
        arr.sort(key=lambda x: x[0])
        
        # Step 2: Check each consecutive pair of meetings for overlap
        for i in range(1, len(arr)):
            # If the start time of the current meeting is less than
            # the end time of the previous meeting, there's an overlap
            if arr[i][0] < arr[i - 1][1]:
                return False
                
        # No overlaps found, so the person can attend all meetings
        return True
        


#{ 
 # Driver Code Starts
if _name_ == '_main_':
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
        ans = obj.canAttend(arr)
        if ans:
            print("true")
        else:
            print("false")

# } Driver Code Ends