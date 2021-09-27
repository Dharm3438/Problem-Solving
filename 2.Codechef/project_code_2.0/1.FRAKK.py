import decimal

for _ in range(int(input())):
    n = int(input())
    a,b = map(int,input().split())
    tot = 0
    res3 =''

    res = decimal.Decimal(a) / decimal.Decimal(b)
    res = str(res)
    pos = res.find('.')
    val3 = res[pos+1:]
    val4 = len(val3)

    if(val4>=n):
        res2 = f'%.{n}f'%res
    else:
        res2 = res
    print(f"res: {res}")
    print(f'res2: {res2}')
    val = res2.split('.')
    dec = val[1]
    for j in dec:
        tot += int(j)
    print(tot)