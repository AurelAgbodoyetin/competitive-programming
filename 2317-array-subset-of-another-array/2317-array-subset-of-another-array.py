#User function Template for python3

def isSubset( a1, a2, n, m):
    count_a1 = {}
    count_a2 = {}
    
    # Count occurrences of elements in array a1
    for num in a1:
        count_a1[num] = count_a1.get(num, 0) + 1
    
    # Count occurrences of elements in array a2
    for num in a2:
        count_a2[num] = count_a2.get(num, 0) + 1
    
    # Check if all elements of a2 are present in a1 with same or greater counts
    for num, count in count_a2.items():
        if num not in count_a1 or count_a1[num] < count:
            return "No"
    
    return "Yes"
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends