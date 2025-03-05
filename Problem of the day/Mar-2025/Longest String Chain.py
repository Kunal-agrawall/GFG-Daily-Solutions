#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)  # Sort words by length
        word_chain = {}  # Dictionary to store longest chain ending at each word
        max_chain = 1  # At least one word is always a valid chain
        
        for word in words:
            word_chain[word] = 1  # Initialize the chain length of this word
            
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]  # Remove one character
                if predecessor in word_chain:
                    word_chain[word] = max(word_chain[word], word_chain[predecessor] + 1)
            
            max_chain = max(max_chain, word_chain[word])
        
        return max_chain



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends