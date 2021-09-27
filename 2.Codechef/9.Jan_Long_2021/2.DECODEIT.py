for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input()))
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    tmp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    
    ans = []

    val=8
    ct=0

    for i in range(n):
        if(ct==4):
            ans.append(a)
            ct=0
            a=[]
            a[:]=tmp[:]
            val=8

        if(arr[i]==0):
            a=a[:val]
            val//=2
        else:
            a=a[val:]
            val//=2

        ct+=1
        #print(a,ans,val,ct)

        
    if(len(a)==0):
        pass
    else:
        ans.append(a)

    for i in range(len(ans)):
        print(ans[i][0],end='')
        #print(a,ct)

    print()
    


   

        

