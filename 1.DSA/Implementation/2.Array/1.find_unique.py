def unique(arr):
    n = len(arr)
    store = dict()
    for i in arr:
        if i in store:
            store[i]+=1
        else:
            store[i]=1

    for key in store:
        if store[key] == 1:
            return key


print(unique([1,1,2,2,3]))