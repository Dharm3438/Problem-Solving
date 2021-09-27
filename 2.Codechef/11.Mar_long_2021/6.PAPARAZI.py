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