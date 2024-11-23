class Solution:
    def maximumProfit(self, prices):
        # Edge case: If prices list is empty or has only one price
        if not prices or len(prices) < 2:
            return 0
        
        # Initialize variables
        min_price = float('inf')  # To track the minimum price encountered so far
        max_profit = 0  # To track the maximum profit
        
        # Iterate through the prices
        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            # Update the maximum profit
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
        


#{ 
 # Driver Code Starts
if _name_ == "_main_":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends