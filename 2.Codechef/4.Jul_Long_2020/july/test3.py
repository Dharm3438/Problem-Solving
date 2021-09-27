for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int, input().split()))
    a.sort()
    days = 1
    i = 0
    while(a[i] >= 0):
        days = days + 1
        if x == a[i]:
            a[i] = 0
            x = x*2
            print(f"x: {x} a[i] {a[i]} days: {days}")
            i = i + 1 
            if i== len(a)-1:
                print(f"x: {x} a[i] {a[i]} days: {days}")
                break
        elif x > a[i] :
            x = a[i] *2
            a[i] = 0
            print(f"x: {x} a[i] {a[i]} days: {days}")
            i = i + 1
            if i == len(a)-1:
                print(f"x: {x} a[i] {a[i]} days: {days}")
                break
            
        elif a[i] > x:
            x = x * 2
            print(f"x: {x} a[i] {a[i]} days: {days}")

        #print(f"x: {x} a[i] {a[i]} days: {days}")    
        
            
    print(days)