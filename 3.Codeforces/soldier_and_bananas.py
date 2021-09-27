values = list(map(int,input().split()))
first_banana = values[0]
dollars = values[1]
bananas = values[2]
price = 0

for i in range(1,bananas+1):
    price = price + (i*first_banana)

required = price - dollars

if(required >= 0):
    print(required)
else:
    print(0)