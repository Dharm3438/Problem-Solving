#1) NOTIME 
n,h,x = map(int,input().split())
arr = list(map(int,input().split()))

flg = 0

for i in range(n):
    if(arr[i]+x>=h):
        flg = 1

if(flg):
    print('YES')
else:
    print('NO')





#2) GROUPS    
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





#3) IRSTXOR

def binToDec(n): 
    return int(n,2) 

for _ in range(int(input())):
    n = int(input())
    bin_val = bin(n)[2:]
    
    A='1'
    B='0'

    i=1
    while(i<len(bin_val)):
        if(bin_val[i]=='1'):
            A+='0'
            B+='1'
        else:
            A+='1'
            B+='1'
        i+=1

    val1 = binToDec(A)
    val2 = binToDec(B)
    print(val1*val2)





#4) SPACEARR
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    arr.sort()
    sumi = 0
    fl = 0

    for i in range(len(arr)):
        if(arr[i]>i+1):
            res = 'Second'
            fl = 1
            break
        else:
            sumi+=abs(arr[i]-i+1) 

    if(fl):
        print(res)
    else:
        if(sumi%2==0):
            res = 'Second'
        else:
            res = 'First'
        print(res)





#5) COLGLF4
import sys
x=100000000
sys.setrecursionlimit(x)

def res_clg_life(n,e,h,a,b,c):
    #global ans
    if(n<=0):
        return 0
        
    global val
    ans = val
    
    #cake only
    if(n<=e and n<=h):
        ans = min(ans,n*c)
    #oml only
    if(2*n<=e):
        ans = min(ans,n*a)
    #shake only
    if(3*n<=h):
        ans = min(ans,n*b)
    #cake and shake
    if((h-n)//2>=1 and (h-n)//2>=n-e):
        if(b-c<0):
            k=min(n-1,(h-n)//2)
            ans = min(ans,(b-c)*k+n*c)
        else:
            k=max(1,n-e)
            ans = min(ans,(b-c)*k+n*c)
    #cake and oml
    if((e-n)>=1 and (e-n)>=n-h):
        if(a-c<0):
            k=min(n-1,(e-n))
            ans = min(ans,(a-c)*k+n*c)
        else:
            k=max(1,n-h)
            ans = min(ans,(a-c)*k+n*c)
    #shake and oml
    if(e//2>=1 and e//2>=(3*n-h+2)//3):
        if(a-b<0):
            k = min(n-1,(e//2))
            ans = min(ans,(a-b)*k+n*b)
        else:
            k = max(1,(3*n-h+2)//3)
            ans = min(ans, (a-b)*k+n*b)
    #cake oml shake (ALL)
    if(e>=3 and h>=4 and n>=3):
        ans = min(ans,a+b+c+res_clg_life(n-3,e-3,h-4,a,b,c)) 
    
    return ans 

val = 10**15

for _ in range(int(input())):
    n,e,h,a,b,c = map(int,input().split())
    #ans = val
    ans2 = res_clg_life(n,e,h,a,b,c)
    if(ans2==val):
        print(-1)
    else:
        print(ans2)

    



#6) PAPARAZI
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if(n<=2):
        print(1)
    else:
        ans = 1
        a = []
        for i in range(n):
            a.append([i,arr[i]])

        b = []
        b.append(a[0])
        b.append(a[1])
        len_b = len(b)

        for j in range(2,n):
            while(len_b>=2):
                slope1 = (b[len_b-1][1]-b[len_b-2][1])/(b[len_b-1][0]-b[len_b-2][0])
                slope2 = (a[j][1]-b[len_b-1][1])/(a[j][0]-b[len_b-1][0])

                if(slope2>=slope1):
                    b.pop()
                    len_b-=1
                else:
                    break
            b.append(a[j])
            len_b+=1
            ans = max(ans,b[len_b-1][0]-b[len_b-2][0])

        print(ans)