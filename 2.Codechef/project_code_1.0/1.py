num = int(input())
required = 0
final_req = 0
possible = []
impossible = []

for i in range(num):
    values = list(map(int,input().split()))
    s = values[0] #100
    n = values[1] #4
    k = values[2] #2
    r = values[3] #2

    required = k
    final_req = required
    for i in range(n-1):
        required = required * r 
        final_req += required

    remaining = s - final_req
    if(remaining>=0):
        print("POSSIBLE",remaining)
        print('')
        possible.append(remaining)
    else:
        print("IMPOSSIBLE",abs(remaining))
        print('')
        impossible.append(abs(remaining))


possible_sum = sum(possible)
impossible_sum = sum(impossible)

if(possible_sum>=impossible_sum):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
