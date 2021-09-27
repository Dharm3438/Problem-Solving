num = int(input())
main_list = []
single = []
for i in range(num):
    friends = int(input())
    relation = int(input())

    for j in range(relation):
        temp_list = list(map(int, input().split()))
        main_list.append(temp_list)
    
    for k in range(friends):
        res1 = any(k in sublist for sublist in main_list)
        if(res1):
            pass
        else:
            single.append(k)

    for l in main_list:
        
        pass
    


        
print(single)