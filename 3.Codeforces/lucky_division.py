number = int(input())

a = [4,7,47,74,447,474,744,774,747,477]
count = 0

for i in a:
    if(number==i or number%i == 0):
        print("YES")
        break
    else:
        count += 1

    if(count==10):
        print("NO")

