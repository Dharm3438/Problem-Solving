def intersect(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    i,j=0,0
    res = []
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]==arr2[j]):
            res.append(arr1[i])
            i+=1
            j+=1
        elif(arr1[i]<arr2[j]):
            i+=1
        else:
            j+=1

    return res   

print(intersect([1,2,3,4,5],[3,4,5,6,7,8])) 