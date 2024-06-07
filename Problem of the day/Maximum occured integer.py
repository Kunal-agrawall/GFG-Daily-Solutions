class Solution:
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        # Create a difference array of size maxx + 2
        diff = [0] * (maxx + 2)
        
        # Applying the difference array technique
        for i in range(n):
            diff[l[i]] += 1
            if r[i] + 1 <= maxx:
                diff[r[i] + 1] -= 1
        
        # Computing the prefix sum and finding the maximum occurring integer
        max_count = diff[0]
        max_index = 0
        current_count = diff[0]
        
        for i in range(1, maxx + 1):
            current_count += diff[i]
            if current_count > max_count:
                max_count = current_count
                max_index = i
        
        return max_index



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends