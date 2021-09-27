for _ in range(int(input())):
    r,c,x = map(int,input().split())
    arr1 = []
    arr2 = []
    for i in range(r):
        arr1.append(list(map(int,input().split())))

    for j in range(r):
        arr2.append(list(map(int,input().split())))

    if(r<x and c<x):
        #means check only if both are same and return true or false
        f=0
        for i in range(r):
            for j in range(c):
                if(arr1[i][j]==arr2[i][j]):
                    pass
                else:
                    f=1
                    break
            if(f==1):
                break
        if(f==1):
            print('NO')
        else:
            print('YES')
    elif(c<x):
        #for only row we will check
        i=0
        f=0
        while(i<c):
            j=0
            while(j<r-x+1):
                if(arr1[j][i]!=arr2[j][i]):
                    dif = arr2[j][i] - arr1[j][i]
                    k=j
                    while(k<j+x):
                        arr1[k][i]+=dif
                        k+=1
                j+=1
            if(j==r-x):
                k=r-x+1
                while(k<r):
                    if(arr1[k][i]!=arr2[k][i]):
                        f=1
                        break
                    if(f):
                        break
                    k+=1
            if(f):
                break
            i+=1
        if(f==1):
            print('NO')
        else:
            print('YES')
    elif(r<x):
        #for only column we will check
        i=0
        f=0
        while(i<r):
            j=0
            #print('first loop')
            while(j<c-x+1):
                #print('second loop')
                if(arr1[i][j]!=arr2[i][j]):
                    dif = arr2[i][j] - arr1[i][j]
                    k=j
                    while(k<j+x):
                        #print('third loop')
                        arr1[i][k]+=dif
                        k+=1
                j+=1
            if(j==c-x):
                k=c-x+1
                while(k<c):
                    #print('fourth loop')
                    if(arr1[i][k]!=arr2[i][k]):
                        f=1
                        break
                    if(f==1):
                        break
                    k+=1
            if(f==1):
                break
            i+=1

        if(f==1):
            print('NO')
        else:
            print('YES')
    elif(r==x and c==x):
        i=0
        f=0
        while(i<c):
            print('1. first loop')
            j=0
            while(j<r-x+1):
                print('1. second loop')
                if(arr1[j][i]!=arr2[j][i]):
                    dif = arr2[j][i] - arr1[j][i]
                    k=j
                    while(k<j+x):
                        print('1 .third loop')
                        arr1[k][i]+=dif
                        k+=1
                j+=1
            i+=1
            
        #now performing col full modification and checking also
        i=0
        f=0
        while(i<r):
            j=0
            print('first loop')
            while(j<c-x+1):
                print('second loop')
                if(arr1[i][j]!=arr2[i][j]):
                    dif = arr2[i][j] - arr1[i][j]
                    k=j
                    while(k<j+x):
                        print('third loop')
                        arr1[i][k]+=dif
                        k+=1
                j+=1
            i+=1

        f=0
        for i in range(r):
            for j in range(c):
                if(arr1[i][j]==arr2[i][j]):
                    pass
                else:
                    f=1
                    break
            if(f==1):
                break
        if(f==1):
            print('NO')
        else:
            print('YES')
    elif(r==x and c>x):
        i=0
        f=0
        while(i<c):
            print('1. first loop')
            j=0
            while(j<r-x+1):
                print('1. second loop')
                if(arr1[j][i]!=arr2[j][i]):
                    dif = arr2[j][i] - arr1[j][i]
                    k=j
                    while(k<j+x):
                        print('1 .third loop')
                        arr1[k][i]+=dif
                        k+=1
                j+=1
            i+=1
            
        #now performing col full modification and checking also
        i=0
        f=0
        while(i<r):
            j=0
            print('first loop')
            while(j<c-x+1):
                print('second loop')
                if(arr1[i][j]!=arr2[i][j]):
                    dif = arr2[i][j] - arr1[i][j]
                    k=j
                    while(k<j+x):
                        print('third loop')
                        arr1[i][k]+=dif
                        k+=1
                j+=1
            if(j==c-x):
                k=c-x+1
                while(k<c):
                    print('fourth loop')
                    if(arr1[i][k]!=arr2[i][k]):
                        f=1
                        break
                    if(f==1):
                        break
                    k+=1
            if(f==1):
                break
            i+=1

        if(f==1):
            print('NO')
        else:
            print('YES')
    elif(c==x and r>x):
        i=0
        f=0
        while(i<r):
            j=0
            print('first loop')
            while(j<c-x+1):
                print('second loop')
                if(arr1[i][j]!=arr2[i][j]):
                    dif = arr2[i][j] - arr1[i][j]
                    k=j
                    while(k<j+x):
                        print('third loop')
                        arr1[i][k]+=dif
                        k+=1
                j+=1
            if(f==1):
                break
            i+=1

        i=0
        f=0
        while(i<c):
            j=0
            while(j<r-x+1):
                if(arr1[j][i]!=arr2[j][i]):
                    dif = arr2[j][i] - arr1[j][i]
                    k=j
                    while(k<j+x):
                        arr1[k][i]+=dif
                        k+=1
                j+=1
            if(j==r-x):
                k=r-x+1
                while(k<r):
                    if(arr1[k][i]!=arr2[k][i]):
                        f=1
                        break
                    if(f):
                        break
                    k+=1
            if(f):
                break
            i+=1


    elif(r>x and c>x):
        #run for row and use that same modified array and run for col and check
        #print('greater row and column')
        i=0
        f=0
        while(i<c):
            print('1. first loop')
            j=0
            while(j<r-x+1):
                print('1. second loop')
                if(arr1[j][i]!=arr2[j][i]):
                    dif = arr2[j][i] - arr1[j][i]
                    k=j
                    while(k<j+x):
                        print('1 .third loop')
                        arr1[k][i]+=dif
                        k+=1
                j+=1
            i+=1
            
        if(f==1):
            print('NO')
        else:
            print('YES')
            
        #now performing col full modification and checking also
        i=0
        f=0
        while(i<r):
            j=0
            print('first loop')
            while(j<c-x+1):
                print('second loop')
                if(arr1[i][j]!=arr2[i][j]):
                    dif = arr2[i][j] - arr1[i][j]
                    k=j
                    while(k<j+x):
                        print('third loop')
                        arr1[i][k]+=dif
                        k+=1
                j+=1
            if(j==c-x):
                k=c-x+1
                while(k<c):
                    print('fourth loop')
                    if(arr1[i][k]!=arr2[i][k]):
                        f=1
                        break
                    if(f==1):
                        break
                    k+=1
            if(f==1):
                break
            i+=1

        if(f==1):
            print('NO')
        else:
            print('YES')
    
    print(arr1)
    print(arr2)