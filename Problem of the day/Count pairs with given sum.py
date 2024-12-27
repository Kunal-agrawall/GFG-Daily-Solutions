 #{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Dictionary to store the frequency of elements
        freq = {}
        count = 0
        
        for num in arr:
            # Calculate the complement that would sum to target
            complement = target - num
            
            # If the complement exists in the dictionary, count the pairs
            if complement in freq:
                count += freq[complement]
            
            # Update the frequency of the current number
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count



    

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends