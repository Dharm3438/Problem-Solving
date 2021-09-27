#1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)

def geometric_sum(k):
    
    if(k==0):
        return 1

    return 1/(2**k) + geometric_sum(k-1)


print(geometric_sum(3))
print(geometric_sum(4))