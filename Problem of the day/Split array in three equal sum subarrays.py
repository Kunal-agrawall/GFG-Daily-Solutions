class Solution:
    
    def findSplit(self, arr):
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, it's impossible to split
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        part_sum, count = 0, 0
        indices = [-1, -1]  # To store the two indices `i` and `j`
        
        # Traverse the array to find two points where part sums are equal to target_sum
        for idx, num in enumerate(arr):
            part_sum += num
            
            # When part_sum matches target_sum, reset it and count up
            if part_sum == target_sum:
                if count == 0:
                    indices[0] = idx  # First boundary
                elif count == 1:
                    indices[1] = idx  # Second boundary
                count += 1
                part_sum = 0  # Reset for the next part
            
            # If we have found two boundaries, break early
            if count == 2:
                break
        
        # Check if both indices were found
        if indices[0] != -1 and indices[1] != -1:
            return indices
        
        # If no solution was found
        return [-1, -1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends