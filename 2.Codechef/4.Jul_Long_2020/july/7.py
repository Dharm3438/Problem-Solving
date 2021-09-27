n, q = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(q):
    x, y, z = map(int, input().split())
    z = z-1
    y = y-1
    if x == 1:
        a[y] = z
    elif x == 2:
        if y > z:
            sumx = a[z]
            temp_sum = sumx
            temp = z+1  # 3
            val = -1
            while(z <= y and temp <= y):
                # print(a[temp])
                if h[z] < h[temp]:
                    sumx = sumx + a[temp]
                    temp = temp + 1
                    val = temp
                    z = z+1
                    #temp_sum = sumx
                    #print(f"sumx: {sumx} temp_sum: {temp_sum} z: {z} y: {y} temp: {temp}")
                else:
                    temp = temp+1

                #print(f"temp {temp}")
            if ((y+1)==val):
                print(sumx)
            else:
                print(-1)
        elif y == z:
            print(a[y])
        elif y < z:
            pass