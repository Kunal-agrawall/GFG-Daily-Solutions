class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        # Step 1: Finding potential candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0
        
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify candidates
        threshold = len(arr) // 3
        result = []
        if arr.count(candidate1) > threshold:
            result.append(candidate1)
        if candidate2 != candidate1 and arr.count(candidate2) > threshold:
            result.append(candidate2)
        
        return sorted(result)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if _name_ == "_main_":
    main()

# } Driver Code Ends