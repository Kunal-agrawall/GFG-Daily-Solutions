class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)  # Use set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string
        
        # Find the min/max word lengths to limit iteration
        min_len = min(map(len, dictionary))
        max_len = max(map(len, dictionary))

        for i in range(min_len, n + 1):  # Start from min word length
            for j in range(max(0, i - max_len), i):  # Limit checks to valid ranges
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Early break if a valid segmentation is found
        
        return dp[n]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends