num = int(input())
main_list = []
polygons = []

for i in range(num):
    friends = int(input())
    relation = int(input())
    friend_list = list(map(int,range(friends)))

    #print(friend_list)

    for j in range(relation):
        temp_list = list(map(int, input().split()))
        main_list.append(temp_list)

    for k in main_list:
        for l in k:
            if(friend_list.count(l)):
                pass
            else:
                polygons.append(l)
    

    print(polygons)

