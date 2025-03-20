class Solution:
    def maxProfit(self, prices):
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0

        for price in prices:
            first_buy = max(first_buy, -price)         # Buy first stock at the lowest price
            first_sell = max(first_sell, first_buy + price)  # Sell first stock for max profit
            second_buy = max(second_buy, first_sell - price)  # Buy second stock after first sell
            second_sell = max(second_sell, second_buy + price)  # Sell second stock for max profit

        return second_sell


#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends