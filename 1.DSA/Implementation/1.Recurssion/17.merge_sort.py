def merge(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        l = arr[:mid]
        merge(l)
        r = arr[mid:]
        merge(r)

        i,j,k = 0,0,0
        while i< len(l) and j<len(r):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        
        while k<len(r):
            arr[k] = r[j]
            j+=1
            k+=1

arr = [9,8,7,6,5,4,3,2,1]
merge(arr)
print(arr)