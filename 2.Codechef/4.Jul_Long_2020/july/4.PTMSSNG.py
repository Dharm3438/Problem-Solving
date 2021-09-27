for _ in range(int(input())):
    n = int(input())
    x = []
    y = []
    x_val = []
    y_val = []

    for i in range((4*n)-1):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)

    x.sort()
    y.sort()

    for i in range(len(x)-1):
        print(x[i])

        if(x[i]==x[i+1]):
            i += 2
        else:
            x_val.append(x[i])

        if(x == )


    # for i in range(len(x)-1):
    #     if(x[i] in x_val):
    #         x_val.remove(x[i])
    #     else:
    #         x_val.append(x[i])

    #     if(y[i] in y_val):
    #         y_val.remove(y[i])
    #     else:
    #         y_val.append(y[i])

    # print(x_val,y_val)