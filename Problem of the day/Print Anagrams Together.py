class Solution:

    def anagrams(self, arr):
        '''
        words: list of words
        return : list of groups of anagrams {list will be sorted in driver code (not word in group)}
        '''
        from collections import defaultdict

        # Dictionary to group anagrams
        anagram_map = defaultdict(list)

        for word in arr:
            # Sort the word and use it as a key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        # Collect the groups of anagrams in order of their first appearance
        result = []
        for group in anagram_map.values():
            result.append(group)

        return result




#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends