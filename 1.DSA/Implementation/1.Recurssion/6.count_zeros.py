def count(n):
    
    if(n//10<1):
        return 0

    ans = count(n//10)
    if(n%10==0):
        return 1+ans
    else:
        return ans


print(count(10))
print(count(1000))
print(count(102034))