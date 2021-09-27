def subset(arr,i,n,osf):
    if(i==n):
        print(f"[{osf}]")
        return

    subset(arr,i+1,n,osf+str(arr[i])+',')
    subset(arr,i+1,n,osf)    


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    n = len(arr)
    subset(arr,0,n,'')