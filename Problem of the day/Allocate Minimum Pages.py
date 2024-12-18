class Solution:
    
    # Function to check if it is possible to allocate books such that
    # the maximum pages assigned to a student is less than or equal to `max_pages`.
    def isPossible(self, arr, k, max_pages):
        students_required = 1
        current_pages = 0

        for pages in arr:
            if pages > max_pages:
                return False  # A single book has more pages than max_pages, not possible.
            
            if current_pages + pages > max_pages:
                # Assign books to the next student.
                students_required += 1
                current_pages = pages

                if students_required > k:
                    return False
            else:
                current_pages += pages
        
        return True

    # Function to find the minimum number of pages.
    def findPages(self, arr, k):
        n = len(arr)
        
        # If number of students is greater than number of books, allocation isn't possible.
        if k > n:
            return -1
        
        # Define the search space for binary search.
        low = max(arr)  # Minimum possible maximum pages (at least one book per student).
        high = sum(arr)  # Maximum possible maximum pages (all books to one student).
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if it is possible to allocate books with `mid` as the maximum pages.
            if self.isPossible(arr, k, mid):
                result = mid  # Update result and try for a smaller maximum.
                high = mid - 1
            else:
                low = mid + 1
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends