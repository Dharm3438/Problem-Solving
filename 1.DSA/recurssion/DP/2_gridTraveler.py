# importing the sys module
import sys
sys.setrecursionlimit(10**6)

def gridTraveler(i,j,memo={}):
    
    val = str(i) + ',' + str(j)
    val2 = str(j) + ',' + str(i)
    if(val in memo.keys()):
        return memo[val]
    if(val2 in memo.keys()):
        return memo[val2]

    if(i==1 and j==1):
        return 1
    if(i<=0 or j <=0):
        return 0  

    memo[val] = gridTraveler(i-1,j)+gridTraveler(i,j-1)
    memo[val2] = memo[val]
    return memo[val]


print(gridTraveler(900,900))