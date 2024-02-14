#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        # Create dictionaries to store counts of elements in arrays
        count_a = {}
        count_b = {}
        
        # Count occurrences of elements in array A
        for num in A:
            count_a[num] = count_a.get(num, 0) + 1
        
        # Count occurrences of elements in array B
        for num in B:
            count_b[num] = count_b.get(num, 0) + 1
        
        # Check if the dictionaries are equal
        return count_a == count_b



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends