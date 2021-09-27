def count(n):
    if(n<1):
        return 0

    return 1 + count(n//10)

print(count(1))
print(count(10))
print(count(100))