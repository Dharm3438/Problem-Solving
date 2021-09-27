array_ct = [1] * 1000001
md_val=dict()

def eranthosis_method(val):
    global array_ct
    global md_val
    array_guy = [1] * val

    ct=0

    i=2
    while(i*i<=val):
        j=i*2
        if(array_guy[i]==1):
            while(j<=val):
                if(array_guy[j]==0):
                    pass
                else:
                    array_guy[j]=0
                    ct+=1
                j+=i
        i+=1

    return ct
    
    # array_ct[0]=array_ct[1]=0
    # i=2
    # while(i<=val):
    #     array_ct[i]=array_ct[i-1]
    #     if(array_guy[i]==1):
    #         array_ct[i] +=1
    #     i+=1



for _ in range(int(input())):
    x,y = map(int,input().split())

    res=eranthosis_method(x)

    if(res>y):
        print('Divyam')
    else:
        print('Chef')
