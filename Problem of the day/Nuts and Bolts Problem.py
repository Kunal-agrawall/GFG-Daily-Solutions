class Solution:
    def matchPairs(self, n, nuts, bolts):
        # Predefined order
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
        order_map = {char: idx for idx, char in enumerate(order)}
        
        # Sort nuts and bolts based on predefined order
        nuts.sort(key=lambda x: order_map[x])
        bolts.sort(key=lambda x: order_map[x])

# Example usage:
solution = Solution()
nuts = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']
solution.matchPairs(len(nuts), nuts, bolts)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends