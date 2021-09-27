num = int(input())

for i in range(num):
    values = input().split()
    m = values[0]
    n = values[1]

    check_list = list(map(int,n))
    freq = check_list.count(9)
    if(freq == (len(check_list))):
        pairs = len(n)-1 + 1
        tot_pairs = int(m) * pairs
        print(f"{tot_pairs} {m}")
    else:
        pairs = len(n)-1 
        tot_pairs = int(m) * pairs
        print(f"{tot_pairs} {m}")
    

