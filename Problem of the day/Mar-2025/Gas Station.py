class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        total_tank, curr_tank = 0, 0
        start_index = 0

        for i in range(n):
            net_fuel = gas[i] - cost[i]
            total_tank += net_fuel
            curr_tank += net_fuel
            
            if curr_tank < 0:
                # Reset start position to next station
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends