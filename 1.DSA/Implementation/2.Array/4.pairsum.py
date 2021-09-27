def pair(arr,x):
    arr.sort()
    i=0
    j=len(arr)-1
    ct = 0
    while(i<j):
        if(arr[i]+arr[j]==x):

            #code for handling dupliation
            while(i<j and arr[i]==arr[i+1]):
                i+=1
                ct+=1
            while(i<j and arr[j]==arr[j-1]):
                j-=1
                ct+=1
                
            i+=1
            j-=1
            ct+=1
        elif(arr[i]+arr[j]<x):
            i+=1
        else:
            j-=1

    return ct


print(pair([1,2,3,4,4,4,5],9))