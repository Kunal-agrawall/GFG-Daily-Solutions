class Solution:
    def twoSum(self, arr, target):
        # Dictionary to store number and its index
        num_to_index = {}
        
        for i, num in enumerate(arr):
            # Calculate the complement
            complement = target - num
            
            # Check if complement exists in the dictionary
            if complement in num_to_index:
                # Return the indices of the two numbers
                return [num_to_index[complement], i]
            
            # Store the current number and its index in the dictionary
            num_to_index[num] = i
        
        # If no pair is found, return an empty list (or handle accordingly)
        return []


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends