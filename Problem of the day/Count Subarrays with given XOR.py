
class Solution:
    def subarrayXor(self, arr, k):
        # Dictionary to store prefix_xor frequencies
        xor_count = {}
        prefix_xor = 0
        count = 0

        for num in arr:
            # Update prefix XOR
            prefix_xor ^= num

            # If prefix_xor itself is equal to k, increment count
            if prefix_xor == k:
                count += 1

            # If (prefix_xor ^ k) is found in xor_count, 
            # add its frequency to count
            if prefix_xor ^ k in xor_count:
                count += xor_count[prefix_xor ^ k]

            # Update the frequency of prefix_xor in xor_count
            xor_count[prefix_xor] = xor_count.get(prefix_xor, 0) + 1

        return count



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends