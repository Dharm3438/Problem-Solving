import sys

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)

    sumi = 0

    if(len(a)==1):
        if(a[0] == b[0]):
            print(0)
            sys.exit(0)
        else:
            print(-1)
            sys.exit(0)

    if(a==b):
        print(0)
        sys.exit(0)
    else:
        for i in range(len(a)-1):
            if(a[i]==b[i]):
                pass
            else:
                if(a[i]>b[i] and a[i]==a[i+1]):
                    temp = b[i]
                    b[i] = a[i+1]
                    a[i+1] = temp
                    sumi += min(b[i],a[i+1])
                elif(b[i]>a[i] and b[i]==b[i+1]):
                    temp = a[i]
                    a[i] = b[i+1]
                    b[i+1] = temp
                    sumi += min(a[i],b[i+1])

        if(a==b):
            print(sumi)
        else:
            print(-1)
            sys.exit(0)