class Job:
    # Job class which stores profit and deadline.
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Sort the jobs according to the maximum profit first (in descending order)
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # To keep track of free time slots
        result = [False] * n
        
        # To store the result (Sequence of jobs)
        job_sequence = [-1] * n
        
        max_profit = 0
        count_jobs = 0
        
        # Iterate through all given jobs
        for job in Jobs:
            # Find a free slot for this job (we start from the last possible slot)
            for j in range(min(n, job.deadline) - 1, -1, -1):
                if not result[j]:
                    result[j] = True
                    job_sequence[j] = job.id
                    max_profit += job.profit
                    count_jobs += 1
                    break
        
        return count_jobs, max_profit



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends