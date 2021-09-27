def solve(A):
    maxi = -9999999999
    mini =  9999999999
    for i in A:
        maxi = max(maxi,i)
        mini = min(mini,i)
    print(maxi,mini)
    return mini+maxi

print(solve([1,2,3,4]))
print(solve([9]))
print(solve([0,3,7,6,4,0,5,5,6]))
print(solve([0,1,1,0,0,0]))
