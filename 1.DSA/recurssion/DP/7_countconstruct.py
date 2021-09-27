import sys
sys.setrecursionlimit(10**6)

def countconstruct(t,arr,memo={}):
    if(t in memo.keys()):
        return memo[t]
    if(t==''):
        return 1

    totct = 0

    for val in arr:
        if(t.find(val)==0):
            t=t[len(val)-1:]
            suffix = t
            res = countconstruct(suffix,arr,memo)
            totct += res

    memo[t] = totct
    return memo[t]

print(countconstruct('abcdef',['ab','abc','cd','def','abcd','ef']))
print(countconstruct('dhar',['dhar','d','h','a','r','dh']))