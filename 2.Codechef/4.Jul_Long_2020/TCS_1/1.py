for _ in range(int(input())):
    n = int(input())
    sumi = 0
    ct = 0

    while(sumi < n):
        ct += 1
        sumi = ct + sumi

    print(ct, sumi)
