def print_num(n):
    
    if(n==0):
        return

    print_num(n-1)
    print(n, end = ' ')


print_num(10)
print()
print_num(0)
print()
print_num(1)