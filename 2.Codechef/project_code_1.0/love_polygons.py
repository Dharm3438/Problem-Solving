num = int(input())
mi_list = []

for i in range(num):
    friends = int(input())
    relation = int(input())
    for j in range(relation):
        temp_list = list(map(int,input().split())
        mi_list.append(temp_list)

print(mi_list)