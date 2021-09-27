#code
for _ in range(int(input())):
    s = list(map(int,input()))
    
    ct1=0
    ct2=0
        
    for i in range(len(s)):
        if(i%2==0 and s[i]==1):
            ct1+=1
        if(i&1 and  s[i]==1):
            ct2+=1
        if(i%2==0 and s[i]==0):
            ct2+=1
        if(i&1 and s[i]==0):
            ct1+=1
        
    print(min(ct1,ct2))