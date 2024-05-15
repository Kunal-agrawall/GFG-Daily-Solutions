from collections import defaultdict
class Solution:

    # Function to find the parent of the given element
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
            
    # Function to merge two sets by updating the parent pointers
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def accountsMerge(self, accounts):
        self.parents = [i for i in range(len(accounts))]
        setOfEmails = {}
        for index in range(len(accounts)):
            name, emails = accounts[index][0], accounts[index][1:]
            for email in emails:
                if email in setOfEmails:
                    self.union(index, setOfEmails[email])
                setOfEmails[email] = index
        
        ans = defaultdict(list)
        for email, owner in setOfEmails.items():
            ans[self.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '_main_': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends