
def sb( a, n, x):
    # Your code goes here 
    
    i,j,s = 0,0,0
    m = 999999
    
    while(i<=j and j<n):
        while(s<=x and j<n):
            s += a[j]
            j+=1

        while(s>x and i<j):
            m = min(m,j-i)
            s -= a[i]
            i+=1
            
    return m






#{ 
#  Driver Code Starts


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(sb(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends