import math

for _ in range(int(input())):
    chef, rick = map(int, input().split())
    no_chef = math.ceil(chef/9) 
    no_rick = math.ceil(rick/9) 
    #print(no_chef, no_rick)

    if(no_chef == no_rick):
        #print(no_chef, no_rick)
        print(f"1 {no_rick}")
    elif (no_rick > no_chef):
        #print(no_chef, no_rick)
        print(f"0 {no_chef}")
    elif (no_chef > no_rick):
        #print(no_chef, no_rick)
        print(f"1 {no_rick}")

