n = int(input())
x = 0

for i in range(n):
    operation = input()
    if(operation == '++X' or operation == 'X++'):
        x = x+1
    elif(operation == '--X' or operation == 'X--'):
        x = x-1
    else:
        pass

print(x)