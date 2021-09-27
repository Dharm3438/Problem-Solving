for _ in range(int(input())):
    arr = list(map(int,input()))
    
    ct=0
    i=0
    while(i<len(arr)):
        if(arr[i]==0):
            pass
        else:
            while(i<len(arr)-1 and arr[i]==arr[i+1]):
                i+=1
            ct+=1
        i+=1
    print(ct)