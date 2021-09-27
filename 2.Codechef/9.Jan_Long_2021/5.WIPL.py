for _ in range(int(input())):
    n,k = map(int, input().split())
    h = list(map(int, input().split()))

    sumi = sum(h)

    if(sumi<2*k):
        print(-1)
    elif(sumi==2*k):
        print(n)
    elif(sumi>2*k):
        h.sort(reverse=True)
        t = 0
        i=0
        sa=0
        ct=0
        while(i<n):
            sa=sa+h[i]

            if(sa>=k):
                break

            for j in range(i+1,n):
                if(h[j]>=k-sa):
                    t=1
            
            if(t==1):
                sa=sa+h[j]
                h[j],h[i+1]=h[i+1],h[j]

        i=2
        sb=0
        m=0
        while(i<n):
            sb = sb+h[i]

            if(sb>=k):
                break

            for j in range(i+1,n):
                if(h[j]>=k-sb):
                    m=1

            if(m==1):
                sb=sb+h[j]
                h[j],h[j+1]=h[j+1],h[j]

            if(m!=1):
                for j in range(i+1,n):
                    if(h[m]<(k-sb)):
                        break

                h[m],h[i+1]=h[i+1],h[m]

    print(sa,sb)


# 6 16
# 8 7 6 5 4 2

# 8 6 4
# 7 5 2