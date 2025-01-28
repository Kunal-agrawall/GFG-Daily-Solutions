from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Generate all permutations and remove duplicates by using a set
        unique_permutations = set(permutations(s))
        
        # Convert each tuple back to a string and return as a list
        return ["".join(p) for p in unique_permutations]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends