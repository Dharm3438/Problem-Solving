no = int(input())
final_sum = 0
vectors = []

for i in range(no):
    vector = list(map(int, input().split()))
    vectors.append(vector)

x_count = y_count = z_count = 0

for vector in vectors:
    x_count += vector[0]
    y_count += vector[1]
    z_count += vector[2]

if(x_count == y_count == z_count == 0):
    print("YES") 
else:
    print("NO")
