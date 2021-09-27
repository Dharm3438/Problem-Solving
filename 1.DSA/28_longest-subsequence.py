#User function Template for python3

# arr[] : the input array
# N : size of the array arr[]

# return the length of the longest subsequene of consecutive integers
def findLongestConseqSubseq(arr, N):
    #code here
    arr.sort()
    ct = 0
    num=1
    
    for i in range(len(arr)):
        fg1 = 0
        fg2 = 0
        
        if(i < len(arr)-1):
            while(arr[i]==arr[i+1] and arr[i]==num):
                i+=1
                ct+=1
                fg1 = 1
                print(arr[i],ct,num,i)
            
        if(arr[i]==num):
            ct+=1
            i+=1
            fg2 = 1
            
        print(arr[i],ct,num,i)

        num+=1
        
        if(fg1==0 and fg2==0):
            break
        
        

    return ct


# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# import atexit
# import io
# import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register

# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().split()))
        print(findLongestConseqSubseq(a,n))
# } Driver Code Ends