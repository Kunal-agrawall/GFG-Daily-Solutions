def max_sum(a, n):
    # Compute sumA and S0
    sumA = sum(a)
    S0 = sum(i * a[i] for i in range(n))
    
    # Initialize the maximum value with S0
    max_value = S0
    current_sum = S0
    
    # Iterate to find the maximum sum after any number of rotations
    for k in range(1, n):
        current_sum = current_sum + sumA - n * a[n - k]
        if current_sum > max_value:
            max_value = current_sum
    
    return max_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends