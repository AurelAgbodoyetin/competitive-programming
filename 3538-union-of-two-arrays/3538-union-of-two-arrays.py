#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        # Create a set to store the distinct elements
        union_set = set()
        
        # Iterate through array a and add elements to the set
        for num in a:
            union_set.add(num)
        
        # Iterate through array b and add elements to the set
        for num in b:
            union_set.add(num)
        
        # Return the size of the set
        return len(union_set)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends