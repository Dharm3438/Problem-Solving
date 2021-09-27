no = int(input())
values = list(map(str,input()))

count = 0

for i in range(1,len(values)):
    if(values[i]==values[i-1]):
        count += 1

print(count)
