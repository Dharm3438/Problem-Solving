limak, bob = map(int,input().split())
year = 0


if(limak==bob):
    print(1)
else:
    while(limak<bob):
        limak = limak * 3
        bob = bob * 2
        year=year+1
        #print(f"limak: {limak} Bob: {bob} year: {year}")
        
    if(limak==bob):
        print(year+1)
    else:
        print(year)