class Solution:
    def kthElement(self, k, arr1, arr2):
        if len(arr1) > len(arr2):
            return self.kthElement(k, arr2, arr1)

        n, m = len(arr1), len(arr2)
        low, high = max(0, k - m), min(k, n)
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1
            
            l1 = arr1[cut1 - 1] if cut1 > 0 else float('-inf')
            l2 = arr2[cut2 - 1] if cut2 > 0 else float('-inf')
            r1 = arr1[cut1] if cut1 < n else float('inf')
            r2 = arr2[cut2] if cut2 < m else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return -1  # this case should never be reached with valid input




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
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends