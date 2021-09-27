#https://youtu.be/7WqN5LoI2I8?t=365
# Just go and watch best explanation in 8 mins
'''1) Try to bring all positive elements first and all negative elements at last by swapping using two pointer approach then check if all are positive or negative so we will print them directly otherwise we will swap the potive and negative elements alternatively in one pass'''

n = int(input())
arr = list(map(int,input().split()))

i,j=0,n
while(i<=j):
    if(arr[i]<0 and arr[j]>0):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    elif(arr[i]>0 and arr[j]<0):
        i+=1
        j-=1
    elif(arr[i]>0):
        i+=1
    elif(arr[j]<0):
        j-=1

'''if contidion to check if we have all positve elements or all negative elements in array can be checked using i as i after the first iteration will point to the starting point of negative element'''

if(i==0 or i==n):
    for val in arr:
        print(val,end=" ")
else:
    k=0
    while(k<n and i<n):
        arr[k],arr[i]=arr[i],arr[k]
        k+=2
        i+=1

    for val in arr:
        print(val,end=" ")