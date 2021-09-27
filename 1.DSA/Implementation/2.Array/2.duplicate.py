def duplicate(arr):
    store={}
    for i in arr:
        if i in store:
            store[i]+=1
        else:
            store[i]=1

    for key in store:
        if store[key]>1:
            return key


print(duplicate([1,2,3,4,5,6,7,7]))
