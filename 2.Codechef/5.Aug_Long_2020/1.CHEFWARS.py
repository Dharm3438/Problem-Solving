for _ in range(int(input())):
    darth, chef = map(int, input().split())
    while darth>0 and chef>0:
        darth = darth - chef
        chef = chef /2 

    if(darth>0):
        print(0)
    else:
        print(1)
