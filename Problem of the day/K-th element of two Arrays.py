class Solution:
    def kthElement(self, a, b, k):
        # Ensure that we always binary search the smaller array
        if len(a) > len(b):
            a, b = b, a
        
        low, high = 0, min(k, len(a))  # Binary search bounds
        
        while low <= high:
            cut_a = (low + high) // 2  # Partition point in a
            cut_b = k - cut_a          # Partition point in b
            
            # If cut_b is out of bounds, adjust
            if cut_b < 0 or cut_b > len(b):
                if cut_b < 0:
                    high = cut_a - 1
                else:
                    low = cut_a + 1
                continue
            
            # Get the elements on the left and right of the partitions
            left_a = a[cut_a - 1] if cut_a > 0 else float('-inf')
            left_b = b[cut_b - 1] if cut_b > 0 else float('-inf')
            right_a = a[cut_a] if cut_a < len(a) else float('inf')
            right_b = b[cut_b] if cut_b < len(b) else float('inf')
            
            # Check if partitions are valid
            if left_a <= right_b and left_b <= right_a:
                # Return the max of the left partition
                return max(left_a, left_b)
            elif left_a > right_b:
                # Move left in a
                high = cut_a - 1
            else:
                # Move right in a
                low = cut_a + 1
        
        return -1  # This should never happen if inputs are valid



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends