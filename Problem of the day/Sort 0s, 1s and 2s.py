#{ 
 # Driver Code Starts

# } Driver Code Ends


class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                # Swap the mid and low values
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # If mid is 1, just move mid pointer
                mid += 1
            else:  # arr[mid] == 2
                # Swap the mid and high values
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr



        

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends