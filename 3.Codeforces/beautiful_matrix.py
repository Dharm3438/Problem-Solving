# matrix = []
# for _ in range(5):
#     matrix.append(list(map(int, input().split())))

# print(matrix)
# row = 0
# colunm = 0
# for i in range(5):
#     for j in range(5):
#         if matrix[i][j] == 1:
#             row = i
#             colunm = j
#             break
# print(abs(row-2) + abs(colunm-2))

matrix = []

for temp in range(5):
    matrix.append(list(map(int,input().split())))

row = 0
colunm = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            row = i
            colunm = j
            break

print(abs(row-2) + abs(colunm-2))
#1 4
#2 1