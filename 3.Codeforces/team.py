n = int(input())
count = 0

for i in range(n):

    numList = list(map(int, input().strip().split()))
    temp = sum(numList)
    if(temp >= 2):
        count = count+1

print(count)