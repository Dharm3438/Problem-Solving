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

    