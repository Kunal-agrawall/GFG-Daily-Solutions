from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = []
        freq_map = defaultdict(int)
        
        # Initialize the frequency map for the first window
        for i in range(k):
            freq_map[arr[i]] += 1
        
        # Store the count of distinct elements for the first window
        result.append(len(freq_map))
        
        # Slide the window
        for i in range(k, n):
            # Remove the element going out of the window
            freq_map[arr[i - k]] -= 1
            if freq_map[arr[i - k]] == 0:
                del freq_map[arr[i - k]]
            
            # Add the new element coming into the window
            freq_map[arr[i]] += 1
            
            # Append the count of distinct elements in the current window
            result.append(len(freq_map))
        
        return result

#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends