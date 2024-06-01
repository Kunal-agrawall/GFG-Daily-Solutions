from collections import Counter

class Solution:
    def oddEven(self, s: str) -> str:
        freq = Counter(s)
        x = 0
        y = 0
        
        for char, count in freq.items():
            pos = ord(char) - ord('a') + 1  # Position in the alphabet (1-based)
            if pos % 2 == 0 and count % 2 == 0:  # Even position and even frequency
                x += 1
            elif pos % 2 == 1 and count % 2 == 1:  # Odd position and odd frequency
                y += 1
        
        total = x + y
        return "EVEN" if total % 2 == 0 else "ODD"

# Example usage
solution = Solution()



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends