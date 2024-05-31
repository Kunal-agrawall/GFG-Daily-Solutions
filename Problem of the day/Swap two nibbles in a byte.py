class Solution:
    def swapNibbles(self, n: int) -> int:
        # Right shift n by 4 bits to get the high nibble and left shift it by 4 bits to move it to low nibble
        high_nibble = (n >> 4)
        # Mask the low nibble with 0x0F and left shift it by 4 bits to move it to high nibble position
        low_nibble = (n & 0x0F) << 4
        # Combine the two nibbles
        return (high_nibble | low_nibble)

# Example usage
solution = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends