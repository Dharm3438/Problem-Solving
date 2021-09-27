def is_prime(n):
    i=2
    while(i*i<=n):
        if(n%i==0):
            return False
        i+=1
    return True


dp = [0] * 1000001
count = 0
dp[0] = 0
dp[1] = 0
j=2
while(j<=1000001):
    if(is_prime(j)):
        count+=1
    dp[j]=count
    j+=1


for _ in range(int(input())):
    x,y=map(int,input().split())

    if(dp[x]<=y):
        print('Chef')
    else:
        print('Divyam')