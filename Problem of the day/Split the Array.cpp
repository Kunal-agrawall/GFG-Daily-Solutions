//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
public:
    const int MOD = 1e9 + 7;

    int countgroup(vector<int>& arr) {
        int n = arr.size();
        
        // Calculate XOR of all elements
        int totalXor = 0;
        for(int i = 0; i < n; i++) {
            totalXor ^= arr[i];
        }
        
        // If total XOR is non-zero, it's impossible to partition
        if (totalXor != 0) {
            return 0;
        }
        
        // If total XOR is zero, count the number of ways to split the array.
        // We can place a partition between each of the elements.
        long long count = 1;  // There is always at least 1 way (no split).
        
        // Loop over each element and calculate number of splits
        for (int i = 0; i < n - 1; i++) {
            count = (count * 2) % MOD;
        }
        
        return count - 1;  // Subtract 1 because we cannot consider the whole array as one group.
    }
};




//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int ans = obj.countgroup(arr);
        cout << ans << endl;
    }
}

// } Driver Code Ends